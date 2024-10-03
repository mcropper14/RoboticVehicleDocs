import cv2 as cv

class CameraOpen:
    def __init__(self):
        self.capture = cv.VideoCapture(0)
        cv_edition = cv.__version__
        if cv_edition[0] == '3':
            self.capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'XVID'))
        else:
            self.capture.set(cv.CAP_PROP_FOURCC, cv.VideoWriter.fourcc('M', 'J', 'P', 'G'))

    def show_camera_feed(self):
        while True:
            ret, frame = self.capture.read()
            if ret:
                cv.imshow('Camera Feed', frame)

            if cv.waitKey(10) & 0xFF == ord('q'):
                break

        self.capture.release()
        cv.destroyAllWindows()

def main():
    camera = CameraOpen()
    camera.show_camera_feed()

if __name__ == '__main__':
    main()
