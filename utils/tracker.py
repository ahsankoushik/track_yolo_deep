# from deep_.tracker import DeepSortTracker 
from deep_sort_update.deep_sort.tracker import Tracker as DeepSortTracker
from deep_sort_update.tools import generate_detections 
from deep_sort_update.deep_sort.detection import Detection
from deep_sort_update.deep_sort import nn_matching
import numpy as np 

class Tracker():
    tracker = None
    encoder = None
    tracks = None

    def __init__(self) -> None:
        model_dir = '/home/koushik/github/track_yolo_deep/models/mars-small128.pb'
        metric = nn_matching.NearestNeighborDistanceMetric("cosine", 0.4, None)
        self.tracker = DeepSortTracker(metric)
        self.encoder = generate_detections.create_box_encoder(model_dir, batch_size=1)
    

    def update(self, frame, detections):
        if len(detections) == 0:
            self.tracker.predict()
            self.tracker.update([])  
            self.update_tracks()
            return

        bboxes = np.asarray([d[:-1] for d in detections])
        bboxes[:, 2:] = bboxes[:, 2:] - bboxes[:, 0:2]
        scores = [d[-1] for d in detections]
        features = self.encoder(frame, bboxes)
        dets = []
        for bbox_id, bbox in enumerate(bboxes):
            dets.append(Detection(bbox, scores[bbox_id], features[bbox_id]))
        self.tracker.predict()
        self.tracker.update(dets)
        self.update_tracks() 

    def update_tracks(self):
        tracks = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            bbox = track.to_tlbr()

            id = track.track_id

            tracks.append(Track(id, bbox))

        self.tracks = tracks


class Track:
    def __init__(self, id, bbox):
        self.track_id = id
        self.bbox = bbox