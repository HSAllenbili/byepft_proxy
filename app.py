from flask import Flask, request, redirect
from flask_cors import CORS
from http import client
from tools.apis import get_version, list_rule, start_img, start_record, end_img, end_record, my_record, record_detail, \
    get_info

client.HTTPConnection._http_vsn_str = 'HTTP/1.1'

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/', methods=['GET'])
def frontend():
    return redirect("https://hsallenbili.github.io/bye_pft", code=302, Response=None)


# 获取版本信息
@app.route('/getVersion', methods=['GET'])
def get_v():
    return get_version()


#  获取锻炼路线
@app.route('/listRule', methods=['GET'])
def list_r():
    return list_rule(request.headers.get("token"), request.headers.get("tenant"), request.headers.get("ua"))


#  上传开始照片
@app.route('/startImg', methods=['POST'])
def start_i():
    return start_img(request.headers.get("token"), request.headers.get("tenant"), request.headers.get("ua"),
                     request.files['file'])


#  开始运动
@app.route('/startRecord', methods=['POST'])
def start_r():
    return start_record(request.headers.get("token"), request.headers.get("tenant"), request.headers.get("ua"),
                        request.data)


#  上传结束照片
@app.route('/endImg', methods=['POST'])
def end_i():
    return end_img(request.headers.get("token"), request.headers.get("tenant"), request.headers.get("ua"),
                   request.files['file'])


#  结束运动
@app.route('/endRecord', methods=['POST'])
def end_r():
    return end_record(request.headers.get("token"), request.headers.get("tenant"),
                      request.headers.get("ua"), request.data)


#  获取运动记录
@app.route('/myRecord', methods=['POST'])
def my_r():
    return my_record(request.headers.get("token"), request.headers.get("tenant"), request.headers.get("ua"))


#  获取记录详情
@app.route('/recordDetail', methods=['POST'])
def record_d():
    return record_detail(request.headers.get("token"), request.headers.get("tenant"),
                         request.headers.get("ua"), request.data)


#  同步学生信息
@app.route('/getInfo', methods=['GET'])
def get_i():
    return get_info(request.headers.get("token"), request.headers.get("tenant"),
                    request.headers.get("ua"))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=11451)
