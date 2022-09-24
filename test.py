import requests

r = requests.post('http://127.0.0.1:8000/main/predict_query_time_execution/INTO tbl_7094,INTO tbl_7095,from tbl_7095,from tbl_7095,INTO tbl_7105,join tbl_7105,JOIN tbl_33332,JOIN tbl_71741,JOIN tbl_71829,FROM tbl_72236,INTO tbl_385661/')
print(r.content.decode('utf-8'))