"""
test_pattern_04.py — Kiểm thử tự động cơ chế Human-in-the-Loop Breakpoint.
"""
import sys
from pathlib import Path
_cur_dir = Path(__file__).resolve().parent
if str(_cur_dir) not in sys.path:
    sys.path.insert(0, str(_cur_dir))

from hitl_gate import HITLApprovalGateway

def test_auto_approval_under_threshold():
    gateway = HITLApprovalGateway(auto_approve_threshold=5_000_000.0)
    tx = gateway.submit_transaction(
        user_id="USR-01",
        amount=1_200_000.0,
        description="Hoàn tiền vé máy bay hủy trước hạn"
    )
    assert tx.status == "DISBURSED"
    assert len(gateway.pending_tickets) == 0
    assert tx.transaction_id in gateway.completed_history

def test_breakpoint_triggered_and_approved():
    gateway = HITLApprovalGateway(auto_approve_threshold=5_000_000.0)
    # Khoản lớn 25.000.000 VNĐ vượt ngưỡng 5.000.000 VNĐ
    tx = gateway.submit_transaction(
        user_id="USR-VIP",
        amount=25_000_000.0,
        description="Yêu cầu bồi thường tổn thất dịch vụ VIP"
    )
    assert tx.status == "WAITING_APPROVAL"
    assert tx.transaction_id in gateway.pending_tickets

    # Quản lý duyệt
    reviewed = gateway.review_ticket(
        transaction_id=tx.transaction_id,
        decision=True,
        approver_name="Manager_Nguyen"
    )
    assert reviewed.status == "DISBURSED"
    assert reviewed.approver == "Manager_Nguyen"
    assert len(gateway.pending_tickets) == 0

def test_breakpoint_rejected():
    gateway = HITLApprovalGateway(auto_approve_threshold=5_000_000.0)
    tx = gateway.submit_transaction(
        user_id="USR-SUSPICIOUS",
        amount=50_000_000.0,
        description="Chuyển khoản đột xuất ngoài giờ"
    )
    assert tx.status == "WAITING_APPROVAL"

    reviewed = gateway.review_ticket(
        transaction_id=tx.transaction_id,
        decision=False,
        approver_name="Security_Officer",
        note="Giao dịch bất thường cần xác minh trực tiếp"
    )
    assert reviewed.status == "REJECTED"
    assert reviewed.approver == "Security_Officer"
