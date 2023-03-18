#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class SmileSpeedwayCounterClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Smile Speedway (Counter Clockwise)"
        self._ui_description = "The official track for the 2019 AWS DeepRacer Championship Cup finals, this is a moderately challenging track ideal for stepping up your training and experimentation."
        self._ui_length_in_m = 23.12  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "reInvent2019_track_ccw"
        self._track_sector_dividers = [25, 48]
        self._annotations = config.smile_speedway_ccw_annotations
        self._track_width = 1.06

        self._track_waypoints = [(-4.010644522186701, -0.014904827009922905), (-4.021977543830872, -0.1444098949432373),
                                 (-4.013929057207597, -0.27416050905767986), (-4.00315797328949, -0.44780243933200836),
                                 (-3.957123041152954, -0.7483700513839722), (-3.8858211040496826, -1.0440138280391693),
                                 (-3.7855409383773804, -1.3309244513511658), (-3.638569951057434, -1.596728503704071),
                                 (-3.431038975715637, -1.8172049522399902), (-3.1580129861831665, -1.9467395544052124),
                                 (-2.855947971343994, -1.97124844789505), (-2.553408980369568, -1.9412139654159546),
                                 (-2.2532495260238647, -1.8919700384140015), (-1.9529444575309753, -1.8435494303703308),
                                 (-1.6496365070343018, -1.8300610184669495), (-1.3536959886550903, -1.8939964175224304),
                                 (-1.0975515246391296, -2.0555729269981384), (-0.8933531194925308, -2.280313551425934),
                                 (-0.7064874619245529, -2.5200769901275635), (-0.4778580591082573, -2.719834089279175),
                                 (-0.21193711319938302, -2.86650550365448), (0.0780884949490428, -2.9565484523773193),
                                 (0.3802950978279114, -2.9866650104522705), (0.6829740107059479, -2.960359573364258),
                                 (0.9753733575344087, -2.8788225650787354), (1.2458555698394775, -2.740334987640381),
                                 (1.4989129900932312, -2.571724534034729), (1.736661970615387, -2.382096529006958),
                                 (1.9607145190238953, -2.1764184832572937), (2.1728840470314026, -1.9584800004959106),
                                 (2.374594569206238, -1.7308210134506226), (2.5660264492034917, -1.4944514632225032),
                                 (2.7475969791412354, -1.2504194974899292), (2.9199295043945312, -0.9997748136520386),
                                 (3.083382487297058, -0.743250966072083), (3.238088011741638, -0.48135924339294434),
                                 (3.3834489583969116, -0.21416950784623623), (3.5187220573425293, 0.05826454609632492),
                                 (3.6430435180664062, 0.3358643427491188), (3.755795478820801, 0.6183596104383469),
                                 (3.85454785823822, 0.9060318171977997), (3.9351390600204468, 1.1992900371551514),
                                 (3.9934885501861572, 1.4977480173110953), (4.022145986557007, 1.8003795146942128),
                                 (4.002721548080444, 2.1034970283508287), (3.9056595563888545, 2.3903485536575326),
                                 (3.7108498811721806, 2.621520042419433), (3.45353102684021, 2.7821820974349976),
                                 (3.168147087097168, 2.8866034746170044), (2.870792508125305, 2.949784994125366),
                                 (2.5682464838027954, 2.9803719520568848), (2.2641810178756714, 2.985977053642273),
                                 (1.960506021976471, 2.9694894552230835), (1.6592864990234375, 2.928330421447754),
                                 (1.364508032798767, 2.8536614179611206), (1.0776350796222687, 2.7528210878372192),
                                 (0.8077462613582611, 2.6136515140533447), (0.5783787965774536, 2.414201498031616),
                                 (0.39174474962055683, 2.1743075251579285), (0.2513688877224922, 1.90464448928833),
                                 (0.14381219446659088, 1.6201534867286682), (0.03819675743579952, 1.3349115252494834),
                                 (-0.11180774867534637, 1.071129471063614), (-0.3439101614058018, 0.8769778162240982),
                                 (-0.6290005892515182, 0.7712031900882721), (-0.9260895550251007, 0.7052600532770157),
                                 (-1.2285860180854797, 0.6743653789162636), (-1.5310840010643023, 0.7028064206242567),
                                 (-1.8178389668464676, 0.8028287738561638), (-2.088489055633545, 0.941702276468277),
                                 (-2.3689280748367327, 1.058715343475342), (-2.6676734685897845, 1.1142509877681732),
                                 (-2.97171950340271, 1.1110024750232697), (-3.2704330682754534, 1.054005175828933),
                                 (-3.5448285341262817, 0.9239427000284195), (-3.76599657535553, 0.7159343361854553),
                                 (-3.9146920442581177, 0.451342836022377), (-3.995479941368103, 0.15838435664772987),
                                 (-4.010644522186701, -0.014904827009922905)]
