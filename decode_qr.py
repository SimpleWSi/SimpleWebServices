from flask import Flask, request, jsonify
from PIL import Image
import base64
from io import BytesIO
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route('/api/decode_qr', methods=['GET'])
def decode_qr():
    try:
        # Lấy dữ liệu JSON từ yêu cầu
        data = request.json
        if 'image_base64' not in data:
            return jsonify({'error': 'Missing "image_base64" in request data'}), 400

        # Giải mã base64 thành hình ảnh
        image_data = base64.b64decode(data['image_base64'])
        image = Image.open(BytesIO(image_data))

        # Giải mã QR code từ hình ảnh
        decoded_objects = decode(image)

        # Trích xuất nội dung từ QR code
        result = []
        for obj in decoded_objects:
            result.append({'data': obj.data.decode('utf-8'), 'type': obj.type})

        if not result:
            return jsonify({'error': 'No QR code found in the image'}), 404

        # Trả về kết quả dưới dạng JSON
        return jsonify({'qr_codes': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
