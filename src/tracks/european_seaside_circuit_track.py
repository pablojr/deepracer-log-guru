#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class EuropeanSeasideCircuitTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "European Seaside Circuit"
        self._ui_description = "A highly technical track, the European Seaside Circuit’s tight turns weave through a timeless Mediterranean cliffside village, without buildings."
        self._ui_length_in_m = 60.0  # metres
        self._ui_width_in_cm = 128  # centimetres
        self._world_name = "Monaco"
        self._track_sector_dividers = [55, 118, 180]
        self._annotations = config.european_seaside_circuit_annotations
        self._track_width = 1.45

        self._track_waypoints = \
            [(-7.328797578811646, 0.7067412286996826), (-7.174184083938599, 0.9988523125648499),
             (-7.014955043792725, 1.2884796857833862), (-6.852129220962524, 1.5760955214500427),
             (-6.69096302986145, 1.8646469712257385), (-6.549050569534302, 2.133627951145172),
             (-6.420227527618408, 2.360764980316162), (-6.282472848892212, 2.563578486442566),
             (-6.135417461395264, 2.7340999841690063), (-5.977877140045166, 2.8688275814056396),
             (-5.81035041809082, 2.968791961669922), (-5.633065938949585, 3.0333319902420044),
             (-5.446821928024292, 3.0640629529953003), (-5.251659393310547, 3.060586452484131),
             (-5.045768976211548, 3.024727463722229), (-4.825798511505127, 2.9580509662628174),
             (-4.588956356048584, 2.8663644790649414), (-4.31685209274292, 2.7589694261550903),
             (-4.021718144416809, 2.6605225205421448), (-3.7218724489212036, 2.5771239399909973),
             (-3.4001494646072388, 2.5014730095863342), (-3.0785800218582153, 2.4250680208206177),
             (-2.7574269771575928, 2.3469924926757812), (-2.4364190101623535, 2.268289566040039),
             (-2.1156229972839355, 2.18874454498291), (-1.7946394681930542, 2.1099590063095093),
             (-1.4724169969558716, 2.036425471305847), (-1.1480990052223206, 1.972858488559723),
             (-0.8215269446372986, 1.9220375418663025), (-0.49347320199012756, 1.882027506828308),
             (-0.16523528099060059, 1.8431255221366882), (0.15957121597602963, 1.7846184968948364),
             (0.47961319983005524, 1.704276978969574), (0.7935185432434082, 1.6027245819568634),
             (1.1075600385665894, 1.5037027299404144), (1.3076865077018738, 1.4583993554115295),
             (1.5055664777755737, 1.4348017573356628), (1.6923699975013733, 1.436053216457367),
             (1.8664454817771912, 1.4613812565803528), (2.0277739763259888, 1.5097875595092773),
             (2.178537964820862, 1.5850645303726196), (2.313390552997589, 1.6858949661254883),
             (2.4278720021247864, 1.8132139444351196), (2.5151830315589905, 1.9660619497299194),
             (2.566936492919922, 2.1485629677772526), (2.5689350366592407, 2.358330011367798),
             (2.5144699811935425, 2.6066219806671143), (2.4257004261016846, 2.8845890760421753),
             (2.3359305262565613, 3.2552294731140137), (2.3159735798835754, 3.5993000268936157),
             (2.3787535429000854, 3.9212855100631714), (2.478807508945465, 4.290599465370178),
             (2.636470079421997, 4.603878498077393), (2.8344470262527466, 4.881711959838867),
             (3.0565370321273804, 5.138339042663574), (3.2876089811325073, 5.387208461761475),
             (3.5140345096588135, 5.6403584480285645), (3.5140345096588135, 5.6403584480285645),
             (3.7155704498291016, 5.867789030075073), (3.9150513410568237, 6.070695161819458),
             (4.123555541038513, 6.237838506698608), (4.350278377532959, 6.357916831970215),
             (4.597380638122559, 6.43809700012207), (4.853857040405273, 6.455471992492676),
             (5.102698564529419, 6.429849624633789), (5.323245525360107, 6.36712646484375),
             (5.529232978820801, 6.26619815826416), (5.686629056930542, 6.151557445526123),
             (5.822824001312256, 6.024678468704224), (5.938603401184082, 5.889411926269531),
             (6.033949375152588, 5.739620923995972), (6.104636907577515, 5.578918933868408),
             (6.150783538818359, 5.403707981109619), (6.164923906326294, 5.222965478897095),
             (6.1468329429626465, 5.038176536560059), (6.079972505569458, 4.82081151008606),
             (5.97437596321106, 4.61850380897522), (5.8233723640441895, 4.414783954620361),
             (5.634581804275513, 4.2054924964904785), (5.428040027618408, 3.975582003593445),
             (5.241874933242798, 3.7154849767684937), (5.102576971054077, 3.419975996017456),
             (5.015120983123779, 3.1196454763412476), (4.971808433532715, 2.8488609790802),
             (4.960218191146851, 2.585760474205017), (4.977452993392944, 2.3392809629440308),
             (5.023159027099609, 2.1146004796028137), (5.096908330917358, 1.921861469745636),
             (5.196659564971924, 1.7596720457077026), (5.3221518993377686, 1.6261754631996155),
             (5.46985650062561, 1.5239906907081604), (5.630683898925781, 1.4561519622802734),
             (5.807667970657349, 1.418973684310913), (5.991654634475708, 1.4157988727092743),
             (6.173375368118286, 1.4475385546684265), (6.361251354217529, 1.5157389640808105),
             (6.552232980728149, 1.6238649785518646), (6.742959976196289, 1.7797954678535461),
             (6.928569316864014, 1.979457974433899), (7.1327619552612305, 2.2291980385780334),
             (7.3353002071380615, 2.4614279866218567), (7.552741527557373, 2.6543909907341003),
             (7.788616895675659, 2.7964354753494263), (8.033162117004395, 2.8772475719451904),
             (8.27453899383545, 2.8965189456939697), (8.491207122802734, 2.8657994270324707),
             (8.696878433227539, 2.7887370586395264), (8.883398056030273, 2.671844482421875),
             (9.050030708312988, 2.5171889066696167), (9.195130348205566, 2.3260200023651123),
             (9.31544828414917, 2.1004135608673096), (9.404008388519287, 1.8435750007629395),
             (9.44702672958374, 1.5588589906692505), (9.426554679870605, 1.2522504925727844),
             (9.337581634521484, 0.9353834688663483), (9.192826747894287, 0.6319848001003265),
             (8.996197700500488, 0.35549574717879295), (8.740715503692627, 0.12512008845806122),
             (8.460927486419678, -0.07559703290462494), (8.175841569900513, -0.2658586651086807),
             (7.892965793609619, -0.4588608369231224), (7.611706018447876, -0.6587495300918818),
             (7.324141502380371, -0.8574651554226875), (7.013044595718384, -1.0239490866661072),
             (6.681285381317139, -1.146332487463951), (6.335738897323608, -1.230746567249298),
             (5.990506172180176, -1.2988191843032837), (5.643296957015991, -1.334423303604126),
             (5.297202110290527, -1.3324593007564545), (4.961018323898315, -1.2930377125740051),
             (4.627946138381958, -1.2881913483142853), (4.2974913120269775, -1.3248490691184998),
             (3.971156597137451, -1.4057363867759705), (3.6392279863357544, -1.460619181394577),
             (3.3074809312820435, -1.4712965488433838), (2.9761369228363037, -1.4499823153018951),
             (2.649322509765625, -1.400215595960617), (2.3273664712905884, -1.3234277367591858),
             (2.009637951850891, -1.2304291427135468), (1.7677425146102905, -1.1627453565597534),
             (1.5230990052223206, -1.1080912500619888), (1.3532370328903198, -1.0856162011623383),
             (1.195859968662262, -1.0760365426540375), (1.0345217287540436, -1.083674892783165),
             (0.8724515438079834, -1.1083671748638153), (0.711279958486557, -1.152745246887207),
             (0.5507968962192535, -1.209416925907135), (0.39081355929374695, -1.2751052379608154),
             (0.20988519862294197, -1.352755606174469), (0.027120925951749086, -1.4227381646633148),
             (-0.15986499935388565, -1.4767869412899017), (-0.35081079602241516, -1.5067747831344604),
             (-0.5378659963607788, -1.50830939412117), (-0.7263861894607544, -1.4828526973724365),
             (-0.9641014337539673, -1.4054632782936096), (-1.1858603358268738, -1.2872214317321777),
             (-1.4105505347251892, -1.1229303479194641), (-1.6448439955711365, -0.9379797577857971),
             (-1.8947490453720093, -0.7638485766947269), (-2.1554964780807495, -0.5910995323210955),
             (-2.4273550510406494, -0.42916758358478546), (-2.725504517555237, -0.2837444841861725),
             (-2.99622642993927, -0.18140959739685059), (-3.219103455543518, -0.11459633708000183),
             (-3.4286000728607178, -0.0705919861793518), (-3.6258760690689087, -0.04686114192008972),
             (-3.8121869564056396, -0.04533001780509949), (-3.989760994911194, -0.06408235430717468),
             (-4.157929539680481, -0.10413399338722229), (-4.316835522651677, -0.16417834162712333),
             (-4.466385602951046, -0.24498264491557906), (-4.601896524429319, -0.3419640436768511),
             (-4.72392392158508, -0.45354240271262586), (-4.832186937332153, -0.5788427442312241),
             (-4.923211812973023, -0.7173683494329479), (-4.9949941635131845, -0.8676890134811426),
             (-5.046401023864746, -1.022179692983629), (-5.0796074867248535, -1.1705849170684814),
             (-5.093028545379639, -1.3209239840507507), (-5.110311985015869, -1.545432984828949),
             (-5.156613349914551, -1.8119059801101685), (-5.23431396484375, -2.074813961982727),
             (-5.337328910827637, -2.3319250345230103), (-5.440672397613525, -2.5615949630737305),
             (-5.537067413330078, -2.7935789823532104), (-5.601041078567505, -3.0084774494171143),
             (-5.629537582397461, -3.2162104845046997), (-5.62337851524353, -3.4190534353256226),
             (-5.583552598953247, -3.617501974105835), (-5.511371850967407, -3.813294529914856),
             (-5.409692049026489, -4.009515404701233), (-5.285758972167969, -4.2109215259552),
             (-5.15318751335144, -4.420788526535034), (-5.032635450363159, -4.634819030761719),
             (-4.952491044998169, -4.822279453277588), (-4.896421194076538, -5.005449533462524),
             (-4.867075443267822, -5.213198900222778), (-4.872295141220093, -5.416158437728882),
             (-4.910168647766113, -5.610260486602783), (-4.973554372787476, -5.776232004165649),
             (-5.060508966445923, -5.920712471008301), (-5.165009498596191, -6.048253059387207),
             (-5.289099931716919, -6.157153606414795), (-5.434471368789673, -6.242535829544067),
             (-5.604140520095825, -6.297412633895874), (-5.79407811164856, -6.322732925415039),
             (-6.00898551940918, -6.311539173126221), (-6.244884967803955, -6.256653070449829),
             (-6.4949564933776855, -6.147663354873657), (-6.781038045883179, -5.9773054122924805),
             (-7.061333417892456, -5.802093505859375), (-7.340768337249756, -5.625651121139526),
             (-7.619298696517944, -5.4476518630981445), (-7.828180313110352, -5.296770811080933),
             (-8.016002416610718, -5.123382568359375), (-8.15831708908081, -4.937673568725586),
             (-8.257988691329956, -4.7432403564453125), (-8.318733215332031, -4.53918194770813),
             (-8.349838495254517, -4.327398061752319), (-8.358692169189453, -4.073875427246094),
             (-8.348212242126465, -3.7435275316238403), (-8.3358793258667, -3.4132790565490723),
             (-8.341327905654907, -3.082790970802307), (-8.343693256378174, -2.7523809671401978),
             (-8.330488443374634, -2.4221235513687134), (-8.290509700775146, -2.0941930413246155),
             (-8.228468656539917, -1.7695454955101013), (-8.158297777175903, -1.4466065168380737),
             (-8.076175212860107, -1.1264664828777313), (-7.979531764984131, -0.8104383051395416),
             (-7.870174884796143, -0.4985577389597893), (-7.749021291732788, -0.19107545539736748),
             (-7.6169209480285645, 0.11187849193811417), (-7.476149082183838, 0.4108997918665409),
             (-7.328797578811646, 0.7067412286996826)]
