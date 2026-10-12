"""
hitl_gate.py — Cơ chế Human-in-the-Loop (HITL) và Breakpoint phê duyệt an toàn.
Mô phỏng cơ chế state.interrupt() của LangGraph trong môi trường sản xuất.
"""
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
import uuid
import time

@dataclass
class TransactionState:
    transaction_id: str
    user_id: str
    amount: float
    description: str
    status: str = "PENDING"  # PENDING, WAITING_APPROVAL, APPROVED, REJECTED, DISBURSED
    approver: Optional[str] = None
    approval_timestamp: Optional[float] = None
    audit_logs: list = field(default_factory=list)

class HITLApprovalGateway:
    def __init__(self, auto_approve_threshold: float = 5_000_000.0):
        self.threshold = auto_approve_threshold
        self.pending_tickets: Dict[str, TransactionState] = {}
        self.completed_history: Dict[str, TransactionState] = {}

    def submit_transaction(self, user_id: str, amount: float, description: str) -> TransactionState:
        tx_id = f"TX-{uuid.uuid4().hex[:8].upper()}"
        state = TransactionState(
            transaction_id=tx_id,
            user_id=user_id,
            amount=amount,
            description=description
        )
        state.audit_logs.append(f"Khởi tạo giao dịch {amount:,.0f} VNĐ lúc {time.time():.2f}")

        # Kiểm tra ngưỡng Breakpoint an toàn
        if amount <= self.threshold:
            # Tự động phê duyệt
            state.status = "DISBURSED"
            state.audit_logs.append(f"Tự động giải ngân (Khoản tiền <= {self.threshold:,.0f} VNĐ)")
            self.completed_history[tx_id] = state
        else:
            # Kích hoạt Breakpoint ngắt chờ phê duyệt
            state.status = "WAITING_APPROVAL"
            state.audit_logs.append(f"Kích hoạt BREAKPOINT: Vượt ngưỡng an toàn ({self.threshold:,.0f} VNĐ), chờ duyệt.")
            self.pending_tickets[tx_id] = state

        return state

    def review_ticket(self, transaction_id: str, decision: bool, approver_name: str, note: str = "") -> TransactionState:
        if transaction_id not in self.pending_tickets:
            raise KeyError(f"Không tìm thấy ticket {transaction_id} trong danh sách chờ duyệt.")

        state = self.pending_tickets.pop(transaction_id)
        state.approver = approver_name
        state.approval_timestamp = time.time()

        if decision is True:
            state.status = "DISBURSED"
            state.audit_logs.append(f"Đã được phê duyệt bởi {approver_name}. Tiến hành giải ngân ngân hàng.")
        else:
            state.status = "REJECTED"
            state.audit_logs.append(f"Bị từ chối bởi {approver_name}. Lý do: {note}")

        self.completed_history[transaction_id] = state
        return state
