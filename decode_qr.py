from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import base64

def decode_qr_from_base64(image_base64):
    """
    Giải mã QR code từ chuỗi ảnh base64.
    :param image_base64: Chuỗi base64 của ảnh QR code.
    :return: Danh sách các QR code đã giải mã (nếu có).
    """
    try:
        # Giải mã base64 thành dữ liệu nhị phân
        image_data = base64.b64decode(image_base64)
        # Chuyển đổi dữ liệu nhị phân thành hình ảnh
        image = Image.open(BytesIO(image_data))
        # Giải mã QR code
        decoded_objects = decode(image)

        # Trích xuất nội dung QR code
        result = []
        for obj in decoded_objects:
            result.append({'data': obj.data.decode('utf-8'), 'type': obj.type})

        return result

    except Exception as e:
        raise ValueError(f"Error decoding QR code: {str(e)}")
