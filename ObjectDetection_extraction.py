from imageai.Detection import ObjectDetection
import os

# current working directory
exec_path = os.getcwd()

# define detection model
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(exec_path, "models/yolov3.pt"))
detector.loadModel()

# detection function to be used in GUI
def detect(imagePath):
    detections, objects_path = detector.detectObjectsFromImage(
        input_image=os.path.join(exec_path, imagePath),  
        output_image_path= os.path.join(exec_path, "result.jpg"),
        minimum_percentage_probability=30, 
        extract_detected_objects=True)
    
    
    return tuple(zip(detections, objects_path))


