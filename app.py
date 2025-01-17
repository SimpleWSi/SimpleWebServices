from flask import Flask, request, jsonify
from qr_decode import decode_qr_from_base64

# Khởi tạo Flask app
app = Flask(__name__)

@app.route('/api/decode_qr', methods=['POST'])
def decode_qr():
    try:
        # Kiểm tra nếu không có dữ liệu JSON
        if not request.json or 'image_base64' not in request.json:
            return jsonify({'error': 'Missing "image_base64" in request data'}), 400

        # Gọi hàm giải mã QR code từ qr_decode.py
        image_base64 = request.json['image_base64']
        result = decode_qr_from_base64(image_base64)

        # Nếu không tìm thấy QR code
        if not result:
            return jsonify({'error': 'No QR code found in the image'}), 404

        # Trả về kết quả
        return jsonify({'qr_codes': result})

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
