import random
"""
<div id="contentWrapper">
  div id="aboutContainer" class="midWidth divStyle bBg">
    <div id="descCont">
      <h1>Family tree creator</h1>
      
      <p>
        This family creator allows you to create customized faces and link them together by activating lines, adding 
        and dragging other lines and possibly adding more yourself in post editing. The faces are all in a rather 
        cartoony style, but hopefully it'll help you with stories and other works that require different styles.
      </p>

      <h2>Instructions</h2>

      <p>
        This tool is pretty easy to use, at least I hope it is. You simply put together your character by clicking on 
        all the different face pieces and the different colors whenever applicable, enter a name, age, a description or 
        any other information you'd like and then click on either 'Add to top', 'Add to second', 'Add to third' or 'Add 
        to bottom' to add your created character to the family tree canvas. The top is for the oldest generation, like 
        the grandparent, and the bottom is for the youngest generation, like the grandchildren.
        
        You can click on the characters in the family tree to select them (border will turn white) and this'll show you 
        the text you may have entered earlier in the main editing section. If you make any changes to this text make 
        sure you click outside of the box after you're done, this'll make sure the changes are saved.

        You can now also change the look of your selected character like you did before. But there are more functions.
      </p>

      <p>
        - <span style="color: #ff9900;">Randomize:</span> Click this button and a completely randomized character will 
          pop up. Note that this will also randomize any character you may have selected, so make sure you deselect it 
          first (click it again to turn its border orange again).
        - <span style="color: #ff9900;">Top, bottom, left, right connection:</span> After you click on the character in 
          the family tree (its border will turn white) you can click on these 4 buttons to enable a corresponding 
          connection. A short orange line will appear and it'll allow you to connect the characters with each other.

          Click it again and the line will turn into a dotted line. This is for characters that may be adopted, living 
          together without being married or for any other relationship you want to differentiate from a 'normal' 
          relationship.

          Click again and the line will disappear again.
        - <span style="color: #ff9900;">Delete selected:</span> Not a fan of the character you've selected anymore? 
          Click it to select it (border will turn white), then click 'delete selected' and poof! It's gone.
        - <span style="color: #ff9900;">Top, mid and bottom connectors:</span> Click on these and a line will be added 
          between the different sections. These lines can be dragged and resized and are meant to be used to connect 
          any potential parents and siblings together. Simply enable the top and bottom connections of the family 
          members, drag the added line to make sure all lines now connect and you're done.
        - <span style="color: #ff9900;">Clear connectors:</span> Click this to get rid of all the lines you've added 
          previously.
        - <span style="color: #ff9900;">Toggle resize:</span> Click this to get rid of that pesky resize triangle of 
          the connection lines. Or click it again to bring it back in case you need to make any more changes.
        - <span style="color: #ff9900;">Save & load buttons:</span> 5 sets of save and load buttons are available to 
          save your family trees. So up to 5 families can be saved and will be available to load again forever. Or at 
          least until you clear your browser cache and only if you didn't use incognito mode to save your family tree 
          in the first place.
      </p>

      <h2>Saving the image</h2>

      <p>
        If you wish to save the family tree you've created all you have to do is click the 'Turn into image' button and 
        an image will appear below it that looks exactly like what you've created. The only difference being that this 
        is a single image, rather than a whole lot of separate images. Simply right click it, select 'save as' and name 
        it what you wish. That's all there is to it. This only works in modern browsers, so if it's not working for you 
        it could be that you need to update your browser.
      </p>

      <h2>Commercial use</h2>

      <p>
        You're free to use the finished result in commercial projects, as long as I'm credited for it. The individual 
        images cannot be sold, redistributed or in any other way be used for commercial purposes without my permission.

        At the end of the day this site, which I put a lot of time into, is still a means to create an income for 
        myself, so I do have to protect some assets. For more info feel free to contact me.
      </p>

    </div>
  </div>

  <div id="contentContainer" class="midWidth divStyle bBg">
    <div class="contentContainer">
      <div id="treeContainer">
        <div id="charCreator">
          <div id="treeOptions">
            <div class="treeOption" onclick='addChar("toTop")'>Add to top</div>
            <div class="treeOption" onclick='addChar("toMid")'>Add to second</div>
            <div class="treeOption" onclick='addChar("toMids")'>Add to third</div>
            <div class="treeOption" onclick='addChar("toBot")'>Add to bottom</div>

            <div class="treeOption" id="conTop">Top connection</div>
            <div class="treeOption" id="conBot">Bottom connection</div>

            <div class="treeOption" id="conRight">Right connection</div>
            <div class="treeOption" id="conLeft">Left connection</div>

            <div class="treeOption" id="delete">Delete selected</div>

            <div class="treeOption" id="addBrTop">Add top connector</div>
            <div class="treeOption" id="addBrMid">Add mid connector</div>
            <div class="treeOption" id="addBrBot">Add bottom connector</div>

            <div class="treeOption" id="clearCon">Clear connectors</div>
            <div class="treeOption" id="togResize">Toggle resize</div>
          </div>
        </div>
        <div id="famTree">
          <div class="treePart" id="parents"></div>
          <div class="borderPart" id="chPa"></div>
          <div class="treePart" id="children"></div>
          <div class="borderPart" id="gChi"></div>
          <div class="treePart" id="gChild"></div>
          <div class="borderPart" id="ggChi"></div>
          <div class="treePart" id="ggChild"></div>
        </div>
        <div id="saveOptions">
          <div class="saveSet">
            <div class="saveIt" name="sTree1" id="save1">Save 1</div>
            <div class="saveIt" name="sTree1" id="load1">Load 1</div>
          </div>
          <div class="saveSet">
            <div class="saveIt" name="sTree2" id="save2">Save 2</div>
            <div class="saveIt" name="sTree2" id="load2">Load 2</div>
          </div>
          <div class="saveSet">
            <div class="saveIt" name="sTree3" id="save3">Save 3</div>
            <div class="saveIt" name="sTree3" id="load3">Load 3</div>
          </div>
          <div class="saveSet">
            <div class="saveIt" name="sTree4" id="save4">Save 4</div>
            <div class="saveIt" name="sTree4" id="load4">Load 4</div>
          </div>
          <div class="saveSet">
            <div class="saveIt" name="sTree5" id="save5">Save 5</div>
            <div class="saveIt" name="sTree5" id="load5">Load 5</div>
          </div>
        </div>
      </div>
      <div id="canvasCont" style="margin: 0 auto; float: none;">
        <div class="canvasControl">
          <input type="button" value="Turn to image" id="toPic" />
        </div>
      </div>
    </div>
  </div>
</div>
"""


# ttl = 0;
# noEarC = 0;
# ear = 1;
# lastClicked = "";
# lastSel = "";
# resize = "on";
# pick = 0;
# pickH = 0;
# pick2 = 0;
# pick3 = 0;
# pickN = 0;
# pickM = 0;
# ttlScar = 0;
# lastRace = "Human";
# noEar = ["hair13","hair17","hair18","hair22","hair27","hair29","hair31","hair34","hair35","hair37","hair38","hair39"];
m_hair = [
    [(i * 40 + j + 1) for j in range(20)]
    for i in range(16)
]
# mhair = [
# ["13","17","18","1","2","3","4","5","6","7","8","9","10","11","12","14","15","16","19","20"],
# ["53","57","58","41","42","43","44","45","46","47","48","49","50","51","52","54","55","56","59","60"],
# ["93","97","98","81","82","83","84","85","86","87","88","89","90","91","92","94","95","96","99","100"],
# ["133","137","138","121","122","123","124","125","126","127","128","129","130","131","132","134","135","136","139","140"],
# ["173","177","178","161","162","163","164","165","166","167","168","169","170","171","172","174","175","176","179","180"],
# ["213","217","218","201","202","203","204","205","206","207","208","209","210","211","212","214","215","216","219","220"],
# ["253","257","258","241","242","243","244","245","246","247","248","249","250","251","252","254","255","256","259","260"],
# ["293","297","298","281","282","283","284","285","286","287","288","289","290","291","292","294","295","296","299","300"],
# ["333","337","338","321","322","323","324","325","326","327","328","329","330","331","332","334","335","336","339","340"],
# ["373","377","378","361","362","363","364","365","366","367","368","369","370","371","372","374","375","376","379","380"],
# ["413","417","418","401","402","403","404","405","406","407","408","409","410","411","412","414","415","416","419","420"],
# ["453","457","458","441","442","443","444","445","446","447","448","449","450","451","452","454","455","456","459","460"],
# ["493","497","498","481","482","483","484","485","486","487","488","489","490","491","492","494","495","496","499","500"],
# ["533","537","538","521","522","523","524","525","526","527","528","529","530","531","532","534","535","536","539","540"],
# ["573","577","578","561","562","563","524","525","526","527","528","569","570","571","572","574","575","576","579","580"],
# ["613","617","618","601","602","603","604","605","606","607","608","609","610","611","612","614","615","616","619","620"]
# ];
f_hair = [
    [(i * 40 + j + 1 + 20) for j in range(20)]
    for i in range(16)
]
# fhair = [
# ["22","27","29","34","35","37","38","39","21","23","24","25","26","28","30","31","32","33","36","40"],
# ["62","67","69","74","75","77","78","79","61","63","64","65","66","68","70","71","72","73","76","80"],
# ["102","107","109","114","115","117","118","119","101","103","104","105","106","108","110","111","112","113","116","120"],
# ["142","147","149","154","155","157","158","159","141","143","144","145","146","148","150","151","152","153","156","160"],
# ["182","187","189","194","195","197","198","199","181","183","184","185","186","188","190","191","192","193","196","200"],
# ["222","227","229","234","235","237","238","239","221","223","224","225","226","228","230","231","232","233","236","240"],
# ["262","267","269","274","275","277","278","279","261","263","264","265","266","268","270","271","272","273","276","280"],
# ["302","307","309","314","315","317","318","319","301","303","304","305","306","308","310","311","312","313","316","320"],
# ["342","347","349","354","355","357","358","359","341","343","344","345","346","348","350","351","352","353","356","360"],
# ["382","387","389","394","395","397","398","399","381","383","384","385","386","388","390","391","392","393","396","400"],
# ["422","427","429","434","435","437","438","439","421","423","424","425","426","428","430","431","432","433","436","440"],
# ["462","467","469","474","475","477","478","479","461","463","464","465","466","468","470","471","472","473","476","480"],
# ["502","507","509","514","515","517","518","519","501","503","504","505","506","508","510","511","512","513","516","520"],
# ["542","547","549","554","555","557","558","559","541","543","544","545","546","548","550","551","552","553","556","560"],
# ["582","587","589","594","595","597","598","599","581","583","584","585","586","588","590","591","592","593","596","600"],
# ["622","627","629","634","635","637","638","639","621","623","624","625","626","628","630","631","632","633","636","640"]
# ];

faces = ["face{}".format(i + 1) for i in range(22)] \
        + ["mface{}".format(i + 1) for i in range(18)] \
        + ["beards{}".format(i + 1) for i in range(17)]
face_colors = ["faceCl{}".format(i + 1) for i in range(24)]
hairs = [
    [
        "bhair{}".format(i),
        "hair{}".format(i),
    ]
    for i in range(41)
]
hair_colors = ["hairCl{}".format(i + 1) for i in range(16)]
ears = ["ears{}".format(i + 1) for i in range(5)]
eyes = ["eyes{}".format(i + 1) for i in range(40)]
eye_colors = ["eyeCl{}".format(i + 1) for i in range(10)]
eyebrows = ["eb{}".format(i + 1) for i in range(80)]
eyebrow_colors = ["eyebCl{}".format(i + 1) for i in range(16)]
noses = ["nose{}".format(i + 1) for i in range(30)] \
        + ["mstch{}".format(i + 1) for i in range(28)]
nose_colors = ["noseCl{}".format(i + 1) for i in range(16)]
mouths = ["mouth{}".format(i + 1) for i in range(80)]
extras = [None] \
         + ["old{}".format(i + 1) for i in range(11)] \
         + ["eye_sp{}".format(i + 1) for i in range(10)] \
         + ["scar{}".format(i + 1) for i in range(30)]


MALE = 1
FEMALE = 2

NORMAL_EYES = 0
ORC_EYES = 1


class Race:
    name = ""
    long_ears = False


class Human(Race):
    name = "Human"


class Elf(Race):
    name = "elf"
    long_ears = True


class Dwarf(Race):
    name = "Dwarf"


class Halfling(Race):
    name = "Halfling"


class Orc(Race):
    name = "Orc"


class Ear:
    def __init__(self, color=None):
        if color is None:
            color = random.randrange(24)
        self.color = color


class Eyes:
    def __init__(self, color=None, eyes_type=NORMAL_EYES):
        if color is None:
            color = random.randrange(200)
        self.color = color
        self.eyes_type = eyes_type


class Mouth:
    def __init__(self, mouth_id=0):
        if mouth_id is None:
            mouth_id = random.randrange(40)
        self.mouth_id = mouth_id

    @property
    def open(self):
        return self.mouth_id >= 20


class EyesSpecial:
    def __init__(self, special_id=0):
        if special_id is None:
            special_id = random.randrange(10)
        self.special_id = special_id


class FaceSpecial:
    def __init__(self, special_id=0):
        if special_id is None:
            special_id = random.randrange(10)
        self.special_id = special_id


class Hair:
    def __init__(self, hair_id=0):
        self.hair_id = hair_id


class Eyebrows:
    def __init__(self, eb_id=0):
        self.eb_id = eb_id


class Nose:
    def __init__(self, nose_id=None, moustache_id=None):
        if nose_id is None:
            nose_id = random.randrange(30)
        if moustache_id is None:
            moustache_id = random.randrange(28)
        self.nose_id = nose_id
        self.moustache_id = moustache_id

    @property
    def has_moustache(self):
        return self.nose_id >= 30


class Person:
    def __init__(self):
        self.sex = MALE
        self.race = Human

        # self.b_hair = None
        self.head = None
        self.scars = {i + 1: None for i in range(30)}
        self.beard = None
        self.mouth = None
        self.nose = None
        self.eyes = None
        self.eyes_special = None
        self.face_special = None
        self.eyebrows = None
        self.hair = None
        self.ear = None

        self.name = "Name"
        self.age = "Age"
        self.desc = "Make sure to click outside of the text boxes after every change you make to make sure it's saved."

    @property
    def eyes_image(self):
        if self.eyes is None:
            return None

        if self.eyes.eyes_type == ORC_EYES:
            return "../images/npc/eyesOrc{}.png".format(self.eyes.color + 1)

        return "../images/npc/eyes{}.png".format(self.eyes.color + 1)

    @property
    def mouth_image(self):
        if self.mouth is None:
            return None

        return "../images/npc/mouth{}.png".format(self.mouth.mouth_id + 1)

    @property
    def eyes_special_image(self):
        if self.eyes_special is None:
            return None

        return "../images/npc/eyesp{}.png".format(self.eyes_special.special_id + 1)

    @property
    def face_special_image(self):
        if self.face_special is None:
            return None

        return "../images/npc/old{}.png".format(self.face_special.special_id + 1)

    @property
    def hair_image(self):
        if self.hair is None:
            return None

        return "../images/npc/hair{}.png".format(self.hair.hair_id)

    @property
    def hair_background(self):
        if self.hair is None:
            return None

        return "../images/npc/bhair{}.png".format(self.hair.hair_id)

    @property
    def eyebrows_image(self):
        if self.eyebrows is None:
            return None

        return "../images/npc/eb{}.png".format(self.eyebrows.eb_id)

    @property
    def nose_image(self):
        if self.nose is None:
            return None

        if self.nose.has_moustache:
            moustache = random.randrange(1, 29) + (28 * (hair + 1) - 28)
            return "../images/npc/mstch{}.png".format(moustache)
        return "../images/npc/nose{}.png".format(self.nose.nose_id + 1)


def randomPerson(person=None):
    def scars_count(percent):
        if has_scar == 2:
            return random.randrange(1, 6)

        if has_scar == 3:
            return random.randrange(10, 20)

        return random.randrange(1, 2)

    if person is None:
        person = Person()

    for i in range(30):
        person.scars[i] = None

    scar_sl = range(30)
    has_scar = random.randrange(20)
    if has_scar < 5:
        scars = list(scar_sl)
        random.shuffle(scars)
        person.scars = scars[:scars_count(has_scar)]

    person.sex = random.choice([MALE, FEMALE])
    person.race = random.choice([
        Human,
        Elf,
        Dwarf,
        Halfling,
        Orc,
    ])

    ear = Ear()

    eye_tp = random.randrange(5)
    if eye_tp == 1:
        person.eyes = Eyes(eyes_type=ORC_EYES)
    else:
        person.eyes = Eyes(eyes_type=NORMAL_EYES)

    person.mouth = Mouth()

    age = random.randrange(10)
    if age < 3:
        person.eyes_special = EyesSpecial()

        if person.mouth.open:
            person.face_special = FaceSpecial(random.randrange(5))
        else:
            person.face_special = FaceSpecial(random.randrange(10))
    else:
        person.face_special = None
        person.eyes_special = None

    if person.sex == MALE:
        hair = random.choice(m_hair)
        person.hair = Hair(random.choice(hair))

        f_eyebrows = random.randrange(hair)
        s_eyebrows = random.randrange(2)
        person.eyebrows = Eyebrows(f_eyebrows * 2 - s_eyebrows)

        nose = Nose()
        if nose.has_moustache:
            moustache = random.randrange(1, 29) + (28 * (hair + 1) - 28)

            person.eyes_special = None
            person.face_special = None

        beard = random.randrange(5)
        if beard > 2:
            beard = random.randrange(1, 18)
            beards = beard + (17 * (hair + 1) - 17)
            if beard == 7 or beard == 9 or beard == 16:
                person.head = "../images/npc/mhead{}.png".format(1 + (18 * ear - 18))
            else:
                person.head = "../images/npc/mhead{}.png".format(11 + (18 * ear - 18))
            person.beard = "../images/npc/beards{}.png".format(beards)
        else:
            head = random.randrange(1, 19) + (18 * ear - 18)
            person.head = "../images/npc/mhead{}.png".format(head)
            person.beard = None

        if person.hair.hair_id < 3 and not person.race.long_ears:
            person.ear = None
        else:
            person.ear = "../images/npc/ear{}{}.png".format(person.race.name, ear)

    elif person.sex == FEMALE:
        hair = random.choice(f_hair)
        person.hair = Hair(random.choice(hair))

        f_eyebrows = random.choice(hair)
        if f_eyebrows == 0:
            s_eyebrows = 0
        else:
            s_eyebrows = random.randrange(2)
        person.eyebrows = Eyebrows(f_eyebrows * 2 - s_eyebrows)

        person.nose = Nose(random.randrange(1, 30))
        person.beard = None

        head = random.randrange(1, 23) + (22 * ear - 22)
        person.head = "../images/npc/head{}.png".format(head)

        if person.hair.hair_id and not person.race.long_ears:
            person.ear = None
        else:
            person.ear = "../images/npc/ear{}{}.png".format(person.race.name, ear)
    return person


def add_char(click):
    """
	ttl = ttl + 1;
	var clicked = click;
	var choice = "";
	var lineLeft = "<div class=\"lineLeft\" style=\"border: none;\"></div>";
	var lineRight = "<div class=\"lineRight\" style=\"border: none;\"></div>";
	var lineTop = "<div class=\"lineTop\" style=\"border: none;\"></div>";
	var lineBot = "<div class=\"lineBot\" style=\"border: none;\"></div>";
	var scars = "<div class=\"scars\" id=\"scarsC" + ttl + "\"><div class=\"scar1t\"></div><div class=\"scar2t\"></div><div class=\"scar3t\"></div><div class=\"scar4t\"></div><div class=\"scar5t\"></div><div class=\"scar6t\"></div><div class=\"scar7t\"></div><div class=\"scar8t\"></div><div class=\"scar9t\"></div><div class=\"scar10t\"></div><div class=\"scar11t\"></div><div class=\"scar12t\"></div><div class=\"scar13t\"></div><div class=\"scar14t\"></div><div class=\"scar15t\"></div><div class=\"scar16t\"></div><div class=\"scar17t\"></div><div class=\"scar18t\"></div><div class=\"scar19t\"></div><div class=\"scar20t\"></div><div class=\"scar21t\"></div><div class=\"scar22t\"></div><div class=\"scar23t\"></div><div class=\"scar24t\"></div><div class=\"scar25t\"></div><div class=\"scar26t\"></div><div class=\"scar27t\"></div><div class=\"scar28t\"></div><div class=\"scar29t\"></div><div class=\"scar30t\"></div></div>";
	if(clicked === "toBot"){
		choice = "#ggChild";
	}else if(clicked === "toMid"){
		choice = "#children";
	}else if(clicked === "toMids"){
		choice = "#gChild";
	}else if(clicked === "toTop"){
		choice = "#parents";
	}else if(clicked === "null"){
		choice = "#none";
	}
	$("<div class=\"character\" id=\"char" + ttl + "\">" + lineTop + lineLeft +"<div class=\"charTree\" id=\"charTree" + ttl +"\"><div class=\"bhair\" id=\"bhairChar" + ttl + "\"></div><div class=\"head\" id=\"headChar" + ttl + "\"></div>" + scars +"<div class=\"beard\" id=\"beardChar" + ttl + "\"></div><div class=\"mouth\" id=\"mouthChar" + ttl + "\"></div><div class=\"nose\" id=\"noseChar" + ttl + "\"></div><div class=\"eyes\" id=\"eyesChar" + ttl + "\"></div><div class=\"eyesSp\" id=\"eyesSpChar" + ttl + "\"></div><div class=\"faceSp\" id=\"faceSpChar" + ttl + "\"></div><div class=\"eyebrows\" id=\"eyebrowsChar" + ttl + "\"></div><div class=\"hair\" id=\"hairChar" + ttl + "\"></div><div class=\"ear\" id=\"earChar" + ttl + "\"></div><input type=\"text\" class=\"charName\" id=\"charName" + ttl + "\"><input type=\"text\" class=\"charAge\" id=\"charAge" + ttl + "\"><textarea class=\"charDesc\" id=\"charDesc" + ttl +"\"></textarea></div>" + lineRight + lineBot + "</div>").appendTo(choice);

	for(i = 1; i <= 30; i++){
		if($("#scar" + i +"t").prop('style').display === "block"){
			$("#scarsC" + ttl + "> .scar" + i + "t").toggle();
		}
	}
	$("#earChar" + ttl).css({"background-image": $("#ear").css('background-image')});
	$("#headChar" + ttl).css({"background-image": $("#head").css('background-image')});
	$("#hairChar" + ttl).css({"background-image": $("#hair").css('background-image')});
	$("#eyebrowsChar" + ttl).css({"background-image": $("#eyebrows").css('background-image')});
	$("#faceSpChar" + ttl).css({"background-image": $("#faceSp").css('background-image')});
	$("#eyesSpChar" + ttl).css({"background-image": $("#eyesSp").css('background-image')});
	$("#eyesChar" + ttl).css({"background-image": $("#eyes").css('background-image')});
	$("#noseChar" + ttl).css({"background-image": $("#nose").css('background-image')});
	$("#mouthChar" + ttl).css({"background-image": $("#mouth").css('background-image')});
	$("#bhairChar" + ttl).css({"background-image": $("#bhair").css('background-image')});
	$("#beardChar" + ttl).css({"background-image": $("#beard").css('background-image')});
	$("#charName" + ttl).val($("#charName").val());
	$("#charAge" + ttl).val($("#charAge").val());
	$("#charDesc" + ttl).val($("#charDesc").val());
	$(".character").draggable({axis: "x"});

    :param click:
    :return:
    """
    pass


class FamilyTreeGenerator:
    def __init__(self):
        pass

    def colChoice(self):
        """
		var clicked = $(this).attr('id');
		var clickClass = $(this).attr('class');
		if(clicked === "eyebCl1" || clicked === "hairCl1" || clicked === "eyeCl1" || clicked === "noseCl1"){
			pick = 0;
			pick2 = 0;
			pick3 = 0;
			pickN = 0;
		}else if(clicked === "faceCl1"){
			ear = 1;
			$(".fcBg").css({"background-color": "#FBC6AF"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head1.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead11.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead1.png\")"});
			pickH = 0;
			pickM = 0;
		}else if(clicked === "faceCl2"){
			ear = 2;
			$(".fcBg").css({"background-color": "#F0CFCF"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head23.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead29.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead19.png\")"});
			pickH = 22;
			pickM = 18;
		}else if(clicked === "faceCl3"){
			ear = 3;
			$(".fcBg").css({"background-color": "#614033"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head45.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead47.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead37.png\")"});
			pickH = 44;
			pickM = 36;
		}else if(clicked === "faceCl4"){
			ear = 4;
			$(".fcBg").css({"background-color": "#DD9478"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head67.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead65.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead55.png\")"});
			pickH = 66;
			pickM = 54;
		}else if(clicked === "faceCl5"){
			ear = 5;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head89.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead83.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead73.png\")"});
			pickH = 88;
			pickM = 72;
		}else if(clicked === "faceCl6"){
			ear = 6;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head111.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead101.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead91.png\")"});
			pickH = 110;
			pickM = 90;
		}else if(clicked === "faceCl7"){
			ear = 7;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head133.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead119.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead109.png\")"});
			pickH = 132;
			pickM = 108;
		}else if(clicked === "faceCl8"){
			ear = 8;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head155.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead137.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead127.png\")"});
			pickH = 154;
			pickM = 126;
		}else if(clicked === "faceCl9"){
			ear = 9;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head177.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead155.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead145.png\")"});
			pickH = 176;
			pickM = 144;
		}else if(clicked === "faceCl10"){
			ear = 10;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head199.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead173.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead163.png\")"});
			pickH = 198;
			pickM = 162;
		}else if(clicked === "faceCl11"){
			ear = 11;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head221.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead191.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead181.png\")"});
			pickH = 220;
			pickM = 180;
		}else if(clicked === "faceCl12"){
			ear = 12;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head243.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead209.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead199.png\")"});
			pickH = 242;
			pickM = 198;
		}else if(clicked === "faceCl13"){
			ear = 13;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head265.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead227.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead217.png\")"});
			pickH = 264;
			pickM = 216;
		}else if(clicked === "faceCl14"){
			ear = 14;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head287.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead245.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead235.png\")"});
			pickH = 286;
			pickM = 234;
		}else if(clicked === "faceCl15"){
			ear = 15;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head309.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead263.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead253.png\")"});
			pickH = 308;
			pickM = 252;
		}else if(clicked === "faceCl16"){
			ear = 16;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head331.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead281.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead271.png\")"});
			pickH = 330;
			pickM = 270;
		}else if(clicked === "faceCl17"){
			ear = 17;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head353.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead299.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead289.png\")"});
			pickH = 352;
			pickM = 288;
		}else if(clicked === "faceCl18"){
			ear = 18;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head375.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead317.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead307.png\")"});
			pickH = 374;
			pickM = 306;
		}else if(clicked === "faceCl19"){
			ear = 19;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head397.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead335.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead325.png\")"});
			pickH = 396;
			pickM = 324;
		}else if(clicked === "faceCl20"){
			ear = 20;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head419.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead353.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead343.png\")"});
			pickH = 418;
			pickM = 342;
		}else if(clicked === "faceCl21"){
			ear = 21;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head441.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead371.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead361.png\")"});
			pickH = 440;
			pickM = 360;
		}else if(clicked === "faceCl22"){
			ear = 22;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head463.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead389.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead379.png\")"});
			pickH = 462;
			pickM = 378;
		}else if(clicked === "faceCl23"){
			ear = 23;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head485.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead407.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead397.png\")"});
			pickH = 484;
			pickM = 396;
		}else if(clicked === "faceCl24"){
			ear = 24;
			$(".fcBg").css({"background-color": "#D6A28B"});
			$(".faceBg").css({"background-image": "url(\"../images/npc/head507.png\")"});
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead425.png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead415.png\")"});
			pickH = 506;
			pickM = 414;
		}else if(clicked === "eyeCl2"){
			pick = 20;
		}else if(clicked === "eyeCl3" || clicked === "hairCl2" || clicked === "noseCl2"){
			pick = 40;
			pick3 = 17;
			pickN = 28;
		}else if(clicked === "eyeCl4"){
			pick = 60;
		}else if(clicked === "eyeCl5" || clicked === "hairCl3" || clicked === "eyebCl2" || clicked === "noseCl3"){
			pick = 80;
			pick3 = 34;
			pickN = 56;
		}else if(clicked === "eyeCl6"){
			pick = 100;
		}else if(clicked === "eyeCl7" || clicked === "hairCl4" || clicked === "noseCl4"){
			pick = 120;
			pick3 = 51;
			pickN = 84;
		}else if(clicked === "eyeCl8"){
			pick = 140;
		}else if(clicked === "eyeCl9" || clicked === "hairCl5" || clicked === "eyebCl3" || clicked === "noseCl5"){
			pick = 160;
			pick3 = 68;
			pickN = 112;
		}else if(clicked === "eyeCl10"){
			pick = 180;
		}else if(clicked === "hairCl6" || clicked === "noseCl6"){
			pick = 200;
			pick3 = 85;
			pickN = 140;
		}else if(clicked === "hairCl7" || clicked === "eyebCl4" || clicked === "noseCl7"){
			pick = 240;
			pick3 = 102;
			pickN = 168;
		}else if(clicked === "hairCl8" || clicked === "noseCl8"){
			pick = 280;
			pick3 = 119;
			pickN = 196;
		}else if(clicked === "hairCl9" || clicked === "eyebCl5" || clicked === "noseCl9"){
			pick = 320;
			pick3 = 136;
			pickN = 224;
		}else if(clicked === "hairCl10" || clicked === "noseCl10"){
			pick = 360;
			pick3 = 153;
			pickN = 252;
		}else if(clicked === "hairCl11" || clicked === "eyebCl6" || clicked === "noseCl11"){
			pick = 400;
			pick3 = 170;
			pickN = 280;
		}else if(clicked === "hairCl12" || clicked === "noseCl12"){
			pick = 440;
			pick3 = 187;
			pickN = 308;
		}else if(clicked === "hairCl13" || clicked === "eyebCl7" || clicked === "noseCl13"){
			pick = 480;
			pick3 = 204;
			pickN = 336;
		}else if(clicked === "hairCl14" || clicked === "noseCl14"){
			pick = 520;
			pick3 = 221;
			pickN = 364;
		}else if(clicked === "eyebCl8" || clicked === "hairCl15" || clicked === "noseCl15"){
			pick = 560;
			pick3 = 238;
			pickN = 392;
		}else if(clicked === "hairCl16" || clicked === "noseCl16"){
			pick = 600;
			pick3 = 255;
			pickN = 420;
		}else if(clicked === "eyebCl9"){
			pick = 640;
		}else if(clicked === "eyebCl10"){
			pick = 720;
		}else if(clicked === "eyebCl11"){
			pick = 800;
		}else if(clicked === "eyebCl12"){
			pick = 880;
		}else if(clicked === "eyebCl13"){
			pick = 960;
		}else if(clicked === "eyebCl14"){
			pick = 1040;
		}else if(clicked === "eyebCl15"){
			pick = 1120;
		}else if(clicked === "eyebCl16"){
			pick = 1200;
		}
		$("#ears1").css({"background-image": "url(\"../images/npc/earHuman" + ear + ".png\")"});
		$("#ears2").css({"background-image": "url(\"../images/npc/earElf" + ear + ".png\")"});
		$("#ears3").css({"background-image": "url(\"../images/npc/earDwarf" + ear + ".png\")"});
		$("#ears4").css({"background-image": "url(\"../images/npc/earHalfling" + ear + ".png\")"});
		$("#ears5").css({"background-image": "url(\"../images/npc/earOrc" + ear + ".png\")"});
		if(clickClass === "colChoice colEyeb"){
			for(i = 1; i < 81; i++){
				picked = pick + i;
				$("#eb" + i).css({"background-image": "url(\"../images/npc/eb" + picked + ".png\")"});
			}
		}else if(clickClass === "colChoice colHair"){
			for(i = 1; i < 41; i++){
				picked = pick + i;
				$("#hair" + i).css({"background-image": "url(\"../images/npc/hair" + picked + ".png\")"});
				$("#bhair" + i).css({"background-image": "url(\"../images/npc/bhair" + picked + ".png\")"});
			}
			for(i = 1; i < 18; i++){
				picked3 = pick3 + i;
				$("#beards" + i).css({"background-image": "url(\"../images/npc/beards" + picked3 + ".png\")"});
			}
		}else if(clickClass === "colChoice colFace"){
			for(i = 1; i < 23; i++){
				picked = pickH + i;
				$("#face" + i).css({"background-image": "url(\"../images/npc/head" + picked + ".png\")"});
			}
			for(i = 1; i < 19; i++){
				picked = pickM + i;
				$("#mface" + i).css({"background-image": "url(\"../images/npc/mhead" + picked + ".png\")"});
			}
			$(".faceBg1").css({"background-image": "url(\"../images/npc/mhead" + (pickM + 11) + ".png\")"});
			$(".faceBg2").css({"background-image": "url(\"../images/npc/mhead" + (pickM + 1) + ".png\")"});
		}else if(clickClass === "colChoice colEye"){
			for(i = 1; i < 21; i++){
				picked = pick + i;
				$("#eyes" + i).css({"background-image": "url(\"../images/npc/eyes" + picked + ".png\")"});
				$("#eyes" + (20+i)).css({"background-image": "url(\"../images/npc/eyesOrc" + picked + ".png\")"});
			}
		}else if(clickClass === "colChoice colNose"){
			for(i = 1; i < 29; i++){
				picked = pickN + i;
				$("#mstch" + i).css({"background-image": "url(\"../images/npc/mstch" + picked + ".png\")"});
			}
		}

        :return:
        """
        pass

def ready():
    """
    $(".piece, .pieceH, .pieceE, .pieceEb, .pieceN, .pieceM, .pieceO, .pieceEs, .piece face, .piece mface, .piece faceBg1, .piecefaceBg2, .pieceEa").click(function(){
        var clicked = $(this).attr('class');
        var clickBg = $(this).css('background-image');
        if(clicked === "piece"){
            $("#head").css({"background-image": clickBg});
            $("#beard").css({"background-image": "none"});
            $(".faceBg").css({"background-image": clickBg});
            $(".selected > .head").css({"background-image": clickBg});
            $(".selected > .beard").css({"background-image": "none"});
            if(noEarC === 1){
                if(lastRace === "Elf"){
                    $("#ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                    $(".selected > .ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                }else{
                    $("#ear").css({"background-image": "none"});
                    $(".selected > .ear").css({"background-image": "none"});
                }
            }else{
                $("#ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
                $(".selected > .ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
            }
        }else if(clicked === "piece faceBg1"){
            var clkBeard = $(this).children().css('background-image');
            $("#beard").css({"background-image": clkBeard});
            $(".selected > .beard").css({"background-image": clkBeard});
            $("#head").css({"background-image": clickBg});
            $(".selected > .head").css({"background-image": clickBg});
            $(".faceBg").css({"background-image": clickBg});
            if(noEarC === 1){
                if(lastRace === "Elf"){
                    $("#ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                    $(".selected > .ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                }else{
                    $("#ear").css({"background-image": "none"});
                    $(".selected > .ear").css({"background-image": "none"});
                }
            }else{
                $("#ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
                $(".selected > .ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
            }
        }else if(clicked === "piece faceBg2"){
            var clkBeard = $(this).children().css('background-image');
            $("#beard").css({"background-image": clkBeard});
            $(".selected > .beard").css({"background-image": clkBeard});
            $("#head").css({"background-image": clickBg});
            $(".selected > .head").css({"background-image": clickBg});
            $(".faceBg").css({"background-image": clickBg});
            if(noEarC === 1){
                if(lastRace === "Elf"){
                    $("#ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                    $(".selected > .ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                }else{
                    $("#ear").css({"background-image": "none"});
                    $(".selected > .ear").css({"background-image": "none"});
                }
            }else{
                $("#ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
                $(".selected > .ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
            }
        }else if(clicked === "pieceH"){
            noEarC = 0;
            var clickHair = $(this).attr('id');
            $("#hair").css({"background-image": clickBg});
            $(".selected > .hair").css({"background-image": clickBg});
            var bhair = $(this).parent().parent().css('background-image');
            $("#bhair").css({"background-image": bhair});
            $(".selected > .bhair").css({"background-image": bhair});
            for(i = 0; i < noEar.length; i++){
                if(noEar[i] === clickHair){
                    noEarC = 1;
                }
            }
            if(noEarC === 1){
                if(lastRace === "Elf"){
                    $("#ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                    $(".selected > .ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                }else{
                    $("#ear").css({"background-image": "none"});
                    $(".selected > .ear").css({"background-image": "none"});
                }
            }else{
                $("#ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
                $(".selected > .ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
            }
        }else if(clicked === "pieceEa"){
            var clkEar = $(this).attr('id');
            if(clkEar === "ears1"){
                lastRace = "Human";
            }else if(clkEar === "ears2"){
                lastRace = "Elf";
            }else if(clkEar === "ears3"){
                lastRace = "Dwarf";
            }else if(clkEar === "ears4"){
                lastRace = "Halfling";
            }else if(clkEar === "ears5"){
                lastRace = "Orc";
            }
            if(noEarC === 1){
                if(lastRace === "Elf"){
                    $("#ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                    $(".selected > .ear").css({"background-image": "url(\"../images/npc/earhElf" + ear + ".png\")"});
                }else{
                    $("#ear").css({"background-image": "none"});
                    $(".selected > .ear").css({"background-image": "none"});
                }
            }else{
                $("#ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
                $(".selected > .ear").css({"background-image": "url(\"../images/npc/ear" + lastRace + ear + ".png\")"});
            }
        }else if(clicked === "pieceE"){
            $("#eyes").css({"background-image": clickBg});
            $(".selected > .eyes").css({"background-image": clickBg});
        }else if(clicked === "pieceEb"){
            $("#eyebrows").css({"background-image": clickBg});
            $(".selected > .eyebrows").css({"background-image": clickBg});
        }else if(clicked === "pieceN"){
            $("#nose").css({"background-image": clickBg});
            $(".selected > .nose").css({"background-image": clickBg});
        }else if(clicked === "pieceM"){
            $("#mouth").css({"background-image": clickBg});
            $(".selected > .mouth").css({"background-image": clickBg});
        }else if(clicked === "pieceO"){
            $("#faceSp").css({"background-image": clickBg});
            $(".selected > .faceSp").css({"background-image": clickBg});
        }else if(clicked === "pieceEs"){
            $("#eyesSp").css({"background-image": clickBg});
            $(".selected > .eyesSp").css({"background-image": clickBg});
        }else if(clicked === "pieceO pieceEs"){
            $("#eyesSp").css({"background-image": "none"});
            $("#faceSp").css({"background-image": "none"});
            $(".selected > .eyesSp").css({"background-image": "none"});
            $(".selected > .faceSp").css({"background-image": "none"});
        }
    });
    """
    """
    $(".pieceSc").click(function(){
        var clicked = $(this).attr('id');
        $("#" + clicked + "t").toggle();
        $(".selected > .scars > ." + clicked + "t").toggle();
    });
    """
    """
    $("#famTree").on('click', '.charTree', function(){
        if($(this).hasClass("selected")){
            $("div").removeClass("selected");
        }else{
            $("div").removeClass("selected");
            $(this).addClass("selected");
        }
        if(!$(".selected > .scars").length && $(".selected").length){
            var curid = $(".selected").attr('id');
            var curttl = curid.substr(curid.length - 1);
            $(".selected > .head").after("<div class=\"scars\" id=\"scarsC" + curttl + "\"><div class=\"scar1t\"></div><div class=\"scar2t\"></div><div class=\"scar3t\"></div><div class=\"scar4t\"></div><div class=\"scar5t\"></div><div class=\"scar6t\"></div><div class=\"scar7t\"></div><div class=\"scar8t\"></div><div class=\"scar9t\"></div><div class=\"scar10t\"></div><div class=\"scar11t\"></div><div class=\"scar12t\"></div><div class=\"scar13t\"></div><div class=\"scar14t\"></div><div class=\"scar15t\"></div><div class=\"scar16t\"></div><div class=\"scar17t\"></div><div class=\"scar18t\"></div><div class=\"scar19t\"></div><div class=\"scar20t\"></div><div class=\"scar21t\"></div><div class=\"scar22t\"></div><div class=\"scar23t\"></div><div class=\"scar24t\"></div><div class=\"scar25t\"></div><div class=\"scar26t\"></div><div class=\"scar27t\"></div><div class=\"scar28t\"></div><div class=\"scar29t\"></div><div class=\"scar30t\"></div></div>");
        }
        if(!$(".selected > .beard").length && $(".selected").length){
            var curid = $(".selected").attr('id');
            var curttl = curid.substr(curid.length - 1);
            $(".selected > .scars").after("<div class=\"beard\" id=\"beardChar" + curttl + "\"></div>");
        }
        var clkPar = $(this).parent().parent().parent().attr('id');
        lastSel = $(this).attr('id');
        if(clkPar === "parents"){
            lastClicked ="toTop";
        }else if(clkPar === "children"){
            lastClicked ="toMid";
        }else if(clkPar === "gChild"){
            lastClicked ="toBot";
        }else if(clkPar === "ggChild"){
            lastClicked ="toMids";
        }
        $("#ear").css("background-image", $(this).children('.ear').css('background-image'));
        $("#hair").css("background-image", $(this).children('.hair').css('background-image'));
        $("#bhair").css("background-image", $(this).children('.bhair').css('background-image'));
        $("#mouth").css("background-image", $(this).children('.mouth').css('background-image'));
        $("#nose").css("background-image", $(this).children('.nose').css('background-image'));
        $("#eyes").css("background-image", $(this).children('.eyes').css('background-image'));
        $("#faceSp").css("background-image", $(this).children('.faceSp').css('background-image'));
        $("#eyesSp").css("background-image", $(this).children('.eyesSp').css('background-image'));
        $("#eyebrows").css("background-image", $(this).children('.eyebrows').css('background-image'));
        $("#head").css("background-image", $(this).children('.head').css('background-image'));
        $("#beard").css("background-image", $(this).children('.beard').css('background-image'));
        $("#charName").val($(this).children('.charName').val());
        $("#charAge").val($(this).children('.charAge').val());
        $("#charDesc").val($(this).children('.charDesc').val());
        if($(".selected").length){
            for(i = 1; i <= 30; i++){
                if($(".selected > .scars > .scar" + i + "t").prop('style').display === "block"){
                    $("#scar" + i + "t").css({"display": "block"});
                }else{
                    $("#scar" + i + "t").css({"display": "none"});
                }
            }
        }
    });
    """
    """
    $("#conTop, #conRight, #conBot, #conLeft").click(function(){
        var clicked = $(this).attr('id');
        var change ="";
        if(clicked === "conTop"){
            change = ".lineTop";
        }else if(clicked === "conRight"){
            change = ".lineRight";
        }else if(clicked === "conBot"){
            change = ".lineBot";
        }else if(clicked === "conLeft"){
            change = ".lineLeft";
        }
        if($(".selected").parent().children(change).prop('style').border === "none" || $(".selected").parent().children(change).prop('style').border === "medium none" || $(".selected").parent().children(change).prop('style').border === "medium"){
            $(".selected").parent().children(change).css({"border": "1px solid rgb(255, 153, 0)"});
        }else if($(".selected").parent().children(change).prop('style').border === "1px solid rgb(255, 153, 0)"){
            $(".selected").parent().children(change).css({"border": "1px dashed rgb(255, 153, 0)"});
        }else{
            $(".selected").parent().children(change).css({"border": "none"});
        }
    });
    """
    """
    $("#addBrTop").click(function(){
        $("<div class=\"conBorder\"></div>").appendTo("#chPa");
        $(".conBorder").resizable();
        $(".conBorder").draggable({axis: "x"});
        resize = "on";
    });
    """
    """
    $("#addBrMid").click(function(){
        $("<div class=\"conBorder\"></div>").appendTo("#gChi");
        $(".conBorder").resizable();
        $(".conBorder").draggable({axis: "x"});
        resize = "on";
    });
    """
    """
    $("#addBrBot").click(function(){
        $("<div class=\"conBorder\"></div>").appendTo("#ggChi");
        $(".conBorder").resizable();
        $(".conBorder").draggable({axis: "x"});
        resize = "on";
    });
    """
    """
    $("#delete").click(function(){
        $(".selected").parent().remove();
    });
    """
    """
    $("#clearCon").click(function(){
        $(".conBorder").remove();
    });
    """
    """
    $("#togResize").click(function(){
        if(resize === "on"){
            $(".conBorder").resizable("disable");
            resize = "off";
        }else{
            $(".conBorder").resizable("enable");
            $(".conBorder").resizable();
            resize = "on";
        }
    });	
    """
    """
    $("#load1, #load2, #load3, #load4").click(function(){
        var nm = $(this).attr("name");
        $("#famTree").html(window.localStorage["famTreeSave" + nm]);
        $(".conBorder").find('.ui-resizable-handle').remove();
        $(".conBorder").draggable({axis: "x"});
        $(".conBorder").resizable();
        $(".conBorder").resizable("enable");
        $(".character").draggable({axis: "x"});
        $(".charName").each(function(index){
            $(this).val(window.localStorage['charName' + nm + index]);
        });
        $(".charAge").each(function(index){
            $(this).val(window.localStorage['charAge' + nm + index]);
        });
        $(".charDesc").each(function(index){
            $(this).val(window.localStorage['charDesc' + nm + index]);
        });
        resize = "on";
        if($("#ggChild").length === 0){
            $("<div class=\"borderPart\" id=\"ggChi\"></div><div class=\"treePart\" id=\"ggChild\"></div>").appendTo("#famTree");
        }
    });
    """
    """
    $("#save1, #save2, #save3, #save4").click(function(){
        var nm = $(this).attr("name");
        $(".conBorder").resizable();
        $(".conBorder").resizable("enable");
        resize = "on";
        window.localStorage.setItem('famTreeSave' + nm, $("#famTree").html());
        $(".charName").each(function(index){
            window.localStorage.setItem('charName' + nm + index, $(this).val());
        });
        $(".charAge").each(function(index){
            window.localStorage.setItem('charAge' + nm + index, $(this).val());
        });
        $(".charDesc").each(function(index){
            window.localStorage.setItem('charDesc' + nm + index, $(this).val());
        });
    });
    """
    """
    $("#toPic").click(function(){ 
        if($("#canvas").length){
            $("#canvas").remove();
        }
        width = $("#famTree").width();
        $("<canvas id=\"canvas\" width=" + width + " height=693></canvas>").appendTo("#canvasCont");
        canvas = document.getElementById("canvas");
        context = canvas.getContext("2d");
        context.strokeStyle="#ff9900";
        phT = "";
        $($(".charTree > div, .charTree > div > div").get()).each(function(){
            if($(this).css("display") != "none"){
                imgPos = $(this).closest(".character").position();
                var img = new Image();
                img.src = $(this).css("background-image").replace('url(\"','').replace('\")','');
                imgWd = $(this).css("width").replace('px','');
                imgHt = $(this).css("height").replace('px','');
                var mainP = $(this).closest(".treePart").attr('id');
                pHt = $(this).closest(".treePart").height();
                if(mainP === "children"){
                    imgTop = parseInt(imgPos.top) + pHt + 25;
                }else if(mainP === "gChild"){
                    imgTop = parseInt(imgPos.top) + pHt * 2 + 25;
                }else if(mainP === "ggChild"){
                    imgTop = parseInt(imgPos.top) + pHt * 3 + 25;
                }else{
                    imgTop = parseInt(imgPos.top) + 25;
                }
                imgLeft = imgPos.left;
                context.rect(imgLeft + 25,imgTop, imgWd, imgHt);
                context.stroke();
                if($(this).hasClass("eyes") || $(this).hasClass("eyebrows") || $(this).hasClass("eyesSp")){
                    imgTop += 4;
                }
                context.drawImage(img, imgLeft + 25, imgTop, imgWd, imgHt);
            }
        });
        $(".lineBot, .lineTop").each(function(){
            if($(this).css("border") === "1px solid rgb(255, 153, 0)" || $(this).css("border") === "1px dashed rgb(255, 153, 0)"){
                var top = $(this).position().top;
                var left = $(this).closest(".character").position().left + 87.5;
                var mainP = $(this).closest(".treePart").attr('id');
                pHt = $(this).closest(".treePart").height();
                if(mainP === "children"){
                    imgTop = top + pHt;
                }else if(mainP === "gChild"){
                    imgTop = top + pHt * 2;
                }else if(mainP === "ggChild"){
                    imgTop = top + pHt * 3;
                }else{
                    imgTop = top;
                }
                if($(this).css("border") === "1px dashed rgb(255, 153, 0)"){
                    context.setLineDash([3, 3]);
                }else{
                    context.setLineDash([]);
                }
                context.beginPath();
                context.moveTo(left,imgTop);
                context.lineTo(left,imgTop + 25);
                context.lineWidth=2
                context.stroke();
            }
        });
        $(".lineRight, .lineLeft").each(function(){
            if($(this).css("border") === "1px solid rgb(255, 153, 0)" || $(this).css("border") === "1px dashed rgb(255, 153, 0)"){
                var left = $(this).position().left + $(this).closest(".character").position().left;
                var mainP = $(this).closest(".treePart").attr('id');
                pHt = $(this).closest(".treePart").height();
                if(mainP === "children"){
                    imgTop = pHt / 2 + pHt;
                }else if(mainP === "gChild"){
                    imgTop = pHt / 2 + pHt * 2;
                }else if(mainP === "ggChild"){
                    imgTop = pHt / 2 + pHt * 3;
                }else{
                    imgTop = pHt / 2;
                }
                if($(this).css("border") === "1px dashed rgb(255, 153, 0)"){
                    context.setLineDash([3, 3]);
                }else{
                    context.setLineDash([]);
                }
                var top = $(this).position().top;
                context.beginPath();
                context.moveTo(left-1,imgTop);
                context.lineTo(left+25,imgTop);
                context.lineWidth=2
                context.stroke();
            }
        });
        $(".conBorder").each(function(){
            context.setLineDash([]);
            var left = $(this).position().left;
            var wd = $(this).width();
            var mainP = $(this).closest(".borderPart").attr('id');
            if(mainP === "gChi"){
                imgTop = pHt * 2 + 1;
            }else if(mainP === "ggChi"){
                imgTop = pHt * 3 + 1;
            }else{
                imgTop = pHt + 1;
            }
            var top = $(this).position().top;
            if(top < 1000){
                context.beginPath();
                context.moveTo(left,imgTop);
                context.lineTo(left + wd,imgTop);
                context.stroke();
            }
        });
    });
    
    :return: 
    """
    pass
