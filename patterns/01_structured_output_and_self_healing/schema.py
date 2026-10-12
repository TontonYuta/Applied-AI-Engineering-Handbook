"""
schema.py — Các định nghĩa Pydantic V2 mẫu cho dữ liệu có cấu trúc.
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class LineItem(BaseModel):
    item_id: str = Field(description="Mã định danh sản phẩm")
    description: str = Field(description="Tên hoặc mô tả ngắn của sản phẩm")
    quantity: int = Field(gt=0, description="Số lượng mua, phải lớn hơn 0")
    unit_price: float = Field(ge=0.0, description="Đơn giá đơn vị sản phẩm")
    total_amount: float = Field(ge=0.0, description="Tổng giá trị từng mục (quantity * unit_price)")

class InvoiceExtraction(BaseModel):
    invoice_number: str = Field(description="Số hóa đơn (ví dụ: INV-2026-001)")
    vendor_name: str = Field(description="Tên công ty phát hành hóa đơn")
    issue_date: str = Field(description="Ngày lập hóa đơn theo chuẩn ISO-8601 (YYYY-MM-DD)")
    tax_id: Optional[str] = Field(default=None, description="Mã số thuế của doanh nghiệp")
    items: List[LineItem] = Field(description="Danh sách các mặt hàng trên hóa đơn")
    subtotal: float = Field(ge=0.0, description="Tổng tiền trước thuế")
    tax_amount: float = Field(default=0.0, ge=0.0, description="Tiền thuế GTGT")
    grand_total: float = Field(ge=0.0, description="Tổng tiền thanh toán cuối cùng")
