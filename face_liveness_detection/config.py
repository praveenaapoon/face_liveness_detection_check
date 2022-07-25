# Profile detection
detect_frontal_face = r'C:\Users\hi\Desktop\face_detection\face_liveness_detection\profile_detection\haarcascades\haarcascade_frontalface_alt.xml'
detect_perfil_face = r'C:\Users\hi\Desktop\face_detection\face_liveness_detection\profile_detection\haarcascades\haarcascade_profileface.xml'

selfie_path = r'C:\Users\hi\Desktop\face_detection\captured pics'

# Emotion detection model
path_model = r'C:\Users\hi\Desktop\face_detection\face_liveness_detection\emotion_detection\Modelos\model_dropout.hdf5'
# Model parameters, the image must be converted to a 48x48 size in grayscale
w, h = 48, 48
rgb = False
labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']


# define the aspect ratio of the eye
# define the number of consecutive frames that must be below the threshold
EYE_AR_THRESH = 0.23    # baseline

EYE_AR_CONSEC_FRAMES = 1

# eye landmarks
eye_landmarks = r"C:\Users\hi\Desktop\face_detection\face_liveness_detection\blink_detection\model_landmarks\shape_predictor_68_face_landmarks.dat"