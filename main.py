from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, inspect
from datetime import timedelta, datetime
import json

app = Flask(__name__)

app.secret_key = "max"
app.permanent_session_lifetime = timedelta(minutes=60)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(100))
    rank = db.Column(db.String(1))
    gender = db.Column(db.String(1))
    bio = db.Column(db.String(500))
    team = db.Column(db.String(25))

    def __init__(self, name, username, password, email, rank, gender, bio, team):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.rank = rank
        self.gender = gender
        self.bio = bio
        self.team = team

class course(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    pars_of_holes = db.Column(db.String)
    course_stats = db.Column(db.String(1000))

    def __init__(self, course_name, pars_of_holes, course_stats):
        self.course_name = course_name
        self.pars_of_holes = pars_of_holes
        self.course_stats = course_stats

class match(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    match_name = db.Column(db.String(50))
    match_course = db.Column(db.String(50))
    start_time = db.Column(db.String(25))
    end_time = db.Column(db.String(25))
    participating_teams = (db.String(500))
    scores_file = (db.String(50))
    match_code = db.Column(db.Integer)
    match_password = db.Column(db.String())

    def __init__(self, match_name, match_course, start_time, end_time, participating_teams, scores_file, match_code, match_password):
        self.match_name = match_name
        self.match_course = match_course
        self.start_time = start_time
        self.end_time = end_time
        self.participating_teams = participating_teams
        self.scores_file = scores_file
        self.match_code = match_code
        self.match_password = match_password

class edit_score_files():
    def __init__(self, score_file_name):
        self.score_file_name = score_file_name
        self.error_msg = "Error, input not found!"
        
    def return_all_scores(self):
        with open("static/score_files/" + self.score_file_name) as file:
            data = json.load(file)
            return data

    def return_team(self, team):
        with open("static/score_files/" + self.score_file_name) as file:
            data = json.load(file)
            for item in data:
                if item == team:
                    return data[item]
            return self.error_msg

    def sum_team_score(self, team):
        with open("static/score_files/" + self.score_file_name) as file:
            team_score = 0
            data = json.load(file)
            for item in data:
                if item == team:
                    for player in data[item]:
                        team_score = team_score + data[item][player]
                    return team_score
            return self.error_msg

    #working but needs to be shortened up...
    def edit_player_score(self, team, player, new_score):
        with open("static/score_files/" + self.score_file_name) as file:
            data = json.load(file)
            for item in data:
                if item == team:
                    for person in data[item]:
                        print(person)
                        if person == player:
                            data[item][person] = new_score
        with open("static/score_files/" + self.score_file_name, "w") as file:
            json.dump(data, file, indent=3)

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

def sanitize_inputs(string_to_analize):
    invalid_list = ['2 girls 1 cup', '2g1c', '4r5e', '5h1t', '5hit', 'a_s_s', 'a55', 'acrotomophilia', 'alabama hot pocket', 'alaskan pipeline', 'anal', 'anilingus', 'anus', 'apeshit', 'ar5e', 'arrse', 'arse', 'arsehole', 'ass', 'ass-fucker', 'ass-hat', 'ass-jabber', 'ass-pirate', 'assbag', 'assbandit', 'assbanger', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfuck', 'assfucker', 'assfukka', 'assgoblin', 'asshat', 'asshead', 'asshole', 'assholes', 'asshopper', 'assjacker', 'asslick', 'asslicker', 'assmonkey', 'assmunch', 'assmuncher', 'assnigger', 'asspirate', 'assshit', 'assshole', 'asssucker', 'asswad', 'asswhole', 'asswipe', 'auto erotic', 'autoerotic', 'axwound', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'babeland', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', 'ballbag', 'balls', 'ballsack', 'bampot', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaner', 'beaners', 'beastial', 'beastiality', 'beaver cleaver', 'beaver lips', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbos', 'birdlock', 'bitch', 'bitchass', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bitchtits', 'bitchy', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody', 'blow job', 'blow your load', 'blowjob', 'blowjobs', 'blue waffle', 'blumpkin', 'boiolas', 'bollock', 'bollocks', 'bollok', 'bollox', 'bondage', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'booty call', 'breasts', 'breeder', 'brotherfucker', 'brown showers', 'brunette action', 'buceta', 'bugger', 'bukkake', 'bulldyke', 'bullet vibe', 'bullshit', 'bum', 'bumblefuck', 'bung hole', 'bunghole', 'bunny fucker', 'busty', 'butt', 'butt plug', 'butt-pirate', 'buttcheeks', 'buttfucka', 'buttfucker', 'butthole', 'buttmuch', 'buttplug', 'c0ck', 'c0cksucker', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'cawk', 'chesticle', 'chinc', 'chink', 'choad', 'chocolate rosebuds', 'chode', 'cipa', 'circlejerk', 'cl1t', 'cleveland steamer', 'clit', 'clitface', 'clitfuck', 'clitoris', 'clits', 'clover clamps', 'clusterfuck', 'cnut', 'cock', 'cock-sucker', 'cockass', 'cockbite', 'cockburger', 'cockeye', 'cockface', 'cockfucker', 'cockhead', 'cockjockey', 'cockknoker', 'cocklump', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmunch', 'cockmuncher', 'cocknose', 'cocknugget', 'cocks', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cockwaffle', 'cok', 'cokmuncher', 'coksucka', 'coochie', 'coochy', 'coon', 'coons', 'cooter', 'coprolagnia', 'coprophilia', 'cornhole', 'cox', 'cracker', 'crap', 'creampie', 'crotte', 'cum', 'cumbubble', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cummer', 'cumming', 'cums', 'cumshot', 'cumslut', 'cumtart', 'cunilingus', 'cunillingus', 'cunnie', 'cunnilingus', 'cunt', 'cuntass', 'cuntface', 'cunthole', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntrag', 'cunts', 'cuntslut', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'dago', 'damn', 'darkie', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'deggo', 'dendrophilia', 'dick', 'dick-sneeze', 'dickbag', 'dickbeaters', 'dickface', 'dickfuck', 'dickfucker', 'dickhead', 'dickhole', 'dickjuice', 'dickmilkÂ\\xa0', 'dickmonger', 'dicks', 'dickslap', 'dicksucker', 'dicksucking', 'dicktickler', 'dickwad', 'dickweasel', 'dickweed', 'dickwod', 'dike', 'dildo', 'dildos', 'dingleberries', 'dingleberry', 'dink', 'dinks', 'dipshit', 'dirsa', 'dirty pillows', 'dirty sanchez', 'dlck', 'dog style', 'dog-fucker', 'doggie style', 'doggiestyle', 'doggin', 'dogging', 'doggy style', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'donkeyribber', 'doochbag', 'dookie', 'doosh', 'double dong', 'double penetration', 'doublelift', 'douche', 'douche-fag', 'douchebag', 'douchewaffle', 'dp action', 'dry hump', 'duche', 'dumass', 'dumb ass', 'dumbass', 'dumbcunt', 'dumbfuck', 'dumbshit', 'dumshit', 'dvda', 'dyke', 'eat my ass', 'ecchi', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'erotic', 'erotism', 'escort', 'eunuch', 'f u c k', 'f u c k e r', 'f_u_c_k', 'f4nny', 'fag', 'fagbag', 'fagfucker', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggotcock', 'faggs', 'fagot', 'fagots', 'fags', 'fagtard', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'felch', 'felching', 'fellate', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingerbang', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fingering', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'fisting', 'flamer', 'flange', 'foah', 'fook', 'fooker', 'foot fetish', 'footjob', 'frotting', 'fuck', 'fuck buttons', 'fuck off', 'fucka', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbutt', 'fuckbutter', 'fucked', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckheads', 'fuckhole', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktards', 'fucktart', 'fucktwat', 'fuckup', 'fuckwad', 'fuckwhit', 'fuckwit', 'fuckwitt', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'futanari', 'fux', 'fux0r', 'g-spot', 'gang bang', 'gangbang', 'gangbanged', 'gangbangs', 'gay', 'gay sex', 'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'god damn', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'goddamnit', 'gokkun', 'golden shower', 'goo girl', 'gooch', 'goodpoop', 'gook', 'goregasm', 'gringo', 'grope', 'group sex', 'guido', 'guro', 'hand job', 'handjob', 'hard core', 'hard on', 'hardcore', 'hardcoresex', 'heeb', 'hell', 'hentai', 'heshe', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'homo', 'homodumbshit', 'homoerotic', 'honkey', 'hooker', 'hore', 'horniest', 'horny', 'hot carl', 'hot chick', 'hotsex', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack Off', 'jack-off', 'jackass', 'jackoff', 'jaggi', 'jagoff', 'jail bait', 'jailbait', 'jap', 'jelly donut', 'jerk off', 'jerk-off', 'jerkass', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jism', 'jiz', 'jizm', 'jizz', 'juggs', 'jungle bunny', 'junglebunny', 'kawk', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knob', 'knobbing', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kooch', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'kunja', 'kunt', 'kyke', 'l3i+ch', 'l3itch', 'labia', 'lameass', 'lardass', 'leather restraint', 'leather straight jacket', 'lemon party', 'lesbian', 'lesbo', 'lezzie', 'lmfao', 'lolita', 'lovemaking', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'make me come', 'male squirting', 'masochist', 'master-bate', 'masterb8', 'masterbat', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mcfagget', 'menage a trois', 'mick', 'milf', 'minge', 'missionary position', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'mound of venus', 'mr hands', 'muff', 'muff diver', 'muffdiver', 'muffdiving', 'munging', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nambla', 'nawashi', 'nazi', 'negro', 'neonazi', 'nig nog', 'nigaboo', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niglet', 'nimphomania', 'nipple', 'nipples', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'nsfw images', 'nude', 'nudity', 'numbnuts', 'nut sack', 'nutsack', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'orgy', 'p0rn', 'paedophile', 'paki', 'panooch', 'panties', 'panty', 'pawn', 'pecker', 'peckerhead', 'pedobear', 'pedophile', 'pegging', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'phone sex', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'piece of shit', 'pigfucker', 'pimpis', 'piss', 'piss pig', 'pissed', 'pissed off', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'pisspig', 'playboy', 'pleasure chest', 'pole smoker', 'polesmoker', 'pollock', 'ponyplay', 'poof', 'poon', 'poonani', 'poonany', 'poontang', 'poop', 'poop chute', 'poopchute', 'poopuncher', 'porch monkey', 'porchmonkey', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'prince albert piercing', 'pron', 'pthc', 'pube', 'pubes', 'punanny', 'punany', 'punta', 'pusse', 'pussi', 'pussies', 'pussy', 'pussylicking', 'pussys', 'pust', 'puto', 'queaf', 'queef', 'queer', 'queerbait', 'queerhole', 'quim', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', 'renob', 'retard', 'reverse cowgirl', 'rimjaw', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'ruski', 'rusty trombone', 's.o.b.', 's&m', 'sadism', 'sadist', 'sand nigger', 'sandler', 'sandnigger', 'sanger', 'santorum', 'scat', 'schlong', 'scissoring', 'screwing', 'scroat', 'scrote', 'scrotum', 'seks', 'semen', 'sex', 'sexo', 'sexy', 'shag', 'shagger', 'shaggin', 'shagging', 'shaved beaver', 'shaved pussy', 'shemale', 'shi+', 'shibari', 'shit', 'shitass', 'shitbag', 'shitbagger', 'shitblimp', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 'shitdick', 'shite', 'shited', 'shitey', 'shitface', 'shitfaced', 'shitfuck', 'shitfull', 'shithead', 'shithole', 'shithouse', 'shiting', 'shitings', 'shits', 'shitspitter', 'shitstain', 'shitted', 'shitter', 'shitters', 'shittiest', 'shitting', 'shittings', 'shitty', 'shiz', 'shiznit', 'shota', 'shrimping', 'skank', 'skeet', 'skullfuck', 'slag', 'slanteye', 'slut', 'slutbag', 'sluts', 'smeg', 'smegma', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'son-of-a-bitch', 'spac', 'spic', 'spick', 'splooge', 'splooge moose', 'spooge', 'spook', 'spread legs', 'spunk', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'suckass', 'sucks', 'suicide girls', 'sultry women', 'swastika', 'swinger', 't1tt1e5', 't1tties', 'tainted love', 'tard', 'taste my', 'tea bagging', 'teets', 'teez', 'testical', 'testicle', 'threesome', 'throating', 'thundercunt', 'tied up', 'tight white', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'titty', 'tittyfuck', 'tittywank', 'titwank', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'turd', 'tushy', 'tw4t', 'twat', 'twathead', 'twatlips', 'twats', 'twatty', 'twatwaffle', 'twink', 'twinkie', 'two girls one cup', 'twunt', 'twunter', 'unclefucker', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'v14gra', 'v1gra', 'va-j-j', 'vag', 'vagina', 'vajayjay', 'venus mound', 'viagra', 'vibrator', 'violet wand', 'vjayjay', 'vorarephilia', 'voyeur', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wankjob', 'wanky', 'wet dream', 'wetback', 'white power', 'whoar', 'whore', 'whorebag', 'whoreface', 'willies', 'willy', 'wop', 'wrapping men', 'wrinkled starfish', 'xrated', 'xx', 'xxx', 'yaoi', 'yellow showers', 'yiffy', 'zoophilia', 'zubb', 'a$$', 'a$$hole', 'a55hole', 'ahole', 'anal impaler', 'anal leakage', 'analprobe', 'ass fuck', 'ass hole', 'assbang', 'assbanged', 'assbangs', 'assfaces', 'assh0le', 'beatch', 'bimbo', 'bitch tit', 'bitched', 'bloody hell', 'bootee', 'bootie', 'bull shit', 'bullshits', 'bullshitted', 'bullturds', 'bum boy', 'butt fuck', 'buttfuck', 'buttmunch', 'c-0-c-k', 'c-o-c-k', 'c-u-n-t', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'caca', 'cacafuego', 'chi-chi man', 'child-fucker', 'clit licker', 'cock sucker', 'corksucker', 'corp whore', 'crackwhore', 'dammit', 'damned', 'damnit', 'darn', 'dick head', 'dick hole', 'dick shy', 'dick-ish', 'dickdipper', 'dickflipper', 'dickheads', 'dickish', 'f-u-c-k', 'f.u.c.k', 'fist fuck', 'fuck hole', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuck-ass', 'fuck-bitch', 'fuck-tard', 'fuckedup', 'fuckmeat', 'fucknugget', 'fucktoy', 'fuq', 'gassy ass', 'h0m0', 'h0mo', 'ham flap', 'he-she', 'hircismus', 'holy shit', 'hom0', 'hoor', 'jackasses', 'jackhole', 'middle finger', 'moo foo', 'naked', 'p.u.s.s.y.', 'piss off', 'piss-off', 'rubbish', 's-o-b', 's0b', 'shit ass', 'shit fucker', 'shiteater', 'son of a bitch', 'son of a whore', 'two fingers', 'wh0re', 'wh0reface']
    for item in invalid_list:
        if item == string_to_analize:
            return True
    return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/header", methods=['GET'])
def header():
    if 'active_user' in session:
        return render_template("header.html")
    return render_template("error.html", message="Sorry, you do not have access to this page.")

@app.route("/error/<msg>")
def error(msg):
    return render_template("error.html", message=msg)

#needs to render a message when password is incorect. 
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        username_input = request.form['username']
        password_input = request.form['password']
        found_user = users.query.filter_by(username=username_input).first()
        
        if found_user and found_user.username == username_input and found_user.password == password_input:
            session['active_user'] = [found_user.username, found_user.name]
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", message="Username and password were incorrect! Please try again.")

    return render_template("login.html")

@app.route("/create_match")
def create_match():
    if 'active_user' in session:
        return render_template("create_match.html")
    return redirect(url_for('error', msg='Sorry, you do not have access to this page.'))

@app.route("/dashboard", methods=['GET'])
def dashboard():
    if 'active_user' in session:
        return render_template("dashboard.html", name=session['active_user'][1])
    return redirect(url_for('error', msg="Sorry, you do not have access to this page."))


@app.route("/create_account", methods=['POST', 'GET'])
def create_account():
    if request.method == "POST":

        for item in request.form:
            if request.form[item] == "" or sanitize_inputs(request.form[item]):
                return redirect(url_for('error', msg="Your value was either blank or inapropriate. Please input all correct values. The problem is with the field: " + request.form[item]))

        found_username = users.query.filter_by(username=request.form['username']).first()
        found_email = users.query.filter_by(email=request.form['email']).first()
        if found_username or found_email:
            return render_template('create_account.html', message="Sorry, the email or username you entered is already in use.")

        try: 
            new_user = users(request.form['name'], request.form['username'], request.form['password'], request.form['email'], request.form['rank'], request.form['gender'], request.form['bio'], request.form['team'])
            db.session.add(new_user)
            db.session.commit()
        except:
            return redirect(url_for('error', msg="There was a problem adding your account to the database. Please make sure you have inputed all fields. If all else fails. Contact customer suport."))

        return render_template('create_account.html', message="Account created sucessfully!")

    return render_template('create_account.html')

@app.route("/logout")
def logout():
    if 'active_user' in session: 
        session.pop('active_user')
    return redirect(url_for('error', msg="How can you log out... if you are not logged in?"))

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/return_user_data/<password>", methods=['GET'])
def return_user_data(password):
    if password == "123":
        list_of_users = users.query.all()
        dict_to_send = {}
        for item in list_of_users:
            dict_to_send[item._id] = object_as_dict(item)
        return dict_to_send,200
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

if __name__ == "__main__":
    db.create_all()
    app.run('0.0.0.0', port=8000, debug=True)