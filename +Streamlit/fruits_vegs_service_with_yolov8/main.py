import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import cv2

import utils

st.set_page_config(page_title='YOLO Detect example', layout='wide')

@st.cache_resource
def load_model():
    print("-----------------model load")
    return YOLO('model/best.pt')

def draw_result(img, result):
    frame = np.array(img)

    xyxy_list = result.boxes.xyxy.to('cpu').numpy().astype('int32')
    cls_list = result.boxes.cls.to('cpu').numpy().astype('int32')
    conf_list = result.boxes.conf.to('cpu').numpy()
    class_names = result.names
    for xyxy, cls, conf in zip(xyxy_list, cls_list, conf_list):
        pt1, pt2 = xyxy[:2], xyxy[2:]
        txt = f"{class_names[cls]}-{conf*100:.2f}%"
        color = utils.get_color(cls % 10)
        cv2.rectangle(frame, pt1, pt2, color=color)
        cv2.putText(frame, txt, org=(pt1[0], pt1[1]-10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5,
                    color=color, thickness=1, lineType=cv2.LINE_AA)
    return frame 


model = load_model()

###################################### sidebar
image_upload = st.sidebar.file_uploader('Upload Image Here', type=['jpg', 'jpeg', 'png'])

##################################### content
st.title('과일 야채 검출')
col1, col2 = st.columns(2)

if image_upload is not None:
    
    up_image = Image.open(image_upload)
    
    result = model(up_image)[0]
    result_img = draw_result(up_image, result)

    col1.header('원본')
    col1.image(up_image)

    col2.header('결과')
    
    col2.image(result_img, width=560)
else:
    st.write('업로드 하세요')