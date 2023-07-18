from setup import *

            
def archive_match(filename):
    with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "a+") as file:
        file.seek(0)
        json_object = json.dump(Scoring.return_data(filename), file, indent=3)
        file.truncate()

def get_archived_match(filename):
    with open("static/archived_matches/" + str(filename) + "_ARCHIVE.json", "r") as file:
        file.seek(0)
        data = json.load(file)
        return data

def return_admin_data():
    db = sqlite3.connect('instance/webdata.sqlite3')
    data = db.execute("select * from users")
    data_dict = {}

    data_dict[0] = {"name": "Name", "username": "Username", "password": "Password", "email": "Email", "rank": "Rank", "gender": "Gender", "bio": "Bio", "team": "Team", "verified": "Verified", "pic": "Picture File"}
    
    for row in data:
        data_dict[len(data_dict)+1] = {"name": row[1], "username": row[2], "password": row[3], "email": row[4], "rank": row[5], "gender": row[6], "bio": row[7], "team": row[8], "verified": row[9], "pic": row[10]}

    return data_dict

def sanitize_inputs(string_to_analize):
    invalid_list = ['2 girls 1 cup', '2g1c', '4r5e', '5h1t', '5hit', 'a_s_s', 'a55', 'acrotomophilia', 'alabama hot pocket', 'alaskan pipeline', 'anal', 'anilingus', 'anus', 'apeshit', 'ar5e', 'arrse', 'arse', 'arsehole', 'ass', 'ass-fucker', 'ass-hat', 'ass-jabber', 'ass-pirate', 'assbag', 'assbandit', 'assbanger', 'assbite', 'assclown', 'asscock', 'asscracker', 'asses', 'assface', 'assfuck', 'assfucker', 'assfukka', 'assgoblin', 'asshat', 'asshead', 'asshole', 'assholes', 'asshopper', 'assjacker', 'asslick', 'asslicker', 'assmonkey', 'assmunch', 'assmuncher', 'assnigger', 'asspirate', 'assshit', 'assshole', 'asssucker', 'asswad', 'asswhole', 'asswipe', 'auto erotic', 'autoerotic', 'axwound', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'babeland', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack', 'ball sucking', 'ballbag', 'balls', 'ballsack', 'bampot', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm', 'beaner', 'beaners', 'beastial', 'beastiality', 'beaver cleaver', 'beaver lips', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'big black', 'big breasts', 'big knockers', 'big tits', 'bimbos', 'birdlock', 'bitch', 'bitchass', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bitchtits', 'bitchy', 'black cock', 'blonde action', 'blonde on blonde action', 'bloody', 'blow job', 'blow your load', 'blowjob', 'blowjobs', 'blue waffle', 'blumpkin', 'boiolas', 'bollock', 'bollocks', 'bollok', 'bollox', 'bondage', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'booty call', 'breasts', 'breeder', 'brotherfucker', 'brown showers', 'brunette action', 'buceta', 'bugger', 'bukkake', 'bulldyke', 'bullet vibe', 'bullshit', 'bum', 'bumblefuck', 'bung hole', 'bunghole', 'bunny fucker', 'busty', 'butt', 'butt plug', 'butt-pirate', 'buttcheeks', 'buttfucka', 'buttfucker', 'butthole', 'buttmuch', 'buttplug', 'c0ck', 'c0cksucker', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher', 'carpetmuncher', 'cawk', 'chesticle', 'chinc', 'chink', 'choad', 'chocolate rosebuds', 'chode', 'cipa', 'circlejerk', 'cl1t', 'cleveland steamer', 'clit', 'clitface', 'clitfuck', 'clitoris', 'clits', 'clover clamps', 'clusterfuck', 'cnut', 'cock', 'cock-sucker', 'cockass', 'cockbite', 'cockburger', 'cockeye', 'cockface', 'cockfucker', 'cockhead', 'cockjockey', 'cockknoker', 'cocklump', 'cockmaster', 'cockmongler', 'cockmongruel', 'cockmonkey', 'cockmunch', 'cockmuncher', 'cocknose', 'cocknugget', 'cocks', 'cockshit', 'cocksmith', 'cocksmoke', 'cocksmoker', 'cocksniffer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cockwaffle', 'cok', 'cokmuncher', 'coksucka', 'coochie', 'coochy', 'coon', 'coons', 'cooter', 'coprolagnia', 'coprophilia', 'cornhole', 'cox', 'cracker', 'crap', 'creampie', 'crotte', 'cum', 'cumbubble', 'cumdumpster', 'cumguzzler', 'cumjockey', 'cummer', 'cumming', 'cums', 'cumshot', 'cumslut', 'cumtart', 'cunilingus', 'cunillingus', 'cunnie', 'cunnilingus', 'cunt', 'cuntass', 'cuntface', 'cunthole', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntrag', 'cunts', 'cuntslut', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'dago', 'damn', 'darkie', 'date rape', 'daterape', 'deep throat', 'deepthroat', 'deggo', 'dendrophilia', 'dick', 'dick-sneeze', 'dickbag', 'dickbeaters', 'dickface', 'dickfuck', 'dickfucker', 'dickhead', 'dickhole', 'dickjuice', 'dickmilkÂ\\xa0', 'dickmonger', 'dicks', 'dickslap', 'dicksucker', 'dicksucking', 'dicktickler', 'dickwad', 'dickweasel', 'dickweed', 'dickwod', 'dike', 'dildo', 'dildos', 'dingleberries', 'dingleberry', 'dink', 'dinks', 'dipshit', 'dirsa', 'dirty pillows', 'dirty sanchez', 'dlck', 'dog style', 'dog-fucker', 'doggie style', 'doggiestyle', 'doggin', 'dogging', 'doggy style', 'doggystyle', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'donkeyribber', 'doochbag', 'dookie', 'doosh', 'double dong', 'double penetration', 'doublelift', 'douche', 'douche-fag', 'douchebag', 'douchewaffle', 'dp action', 'dry hump', 'duche', 'dumass', 'dumb ass', 'dumbass', 'dumbcunt', 'dumbfuck', 'dumbshit', 'dumshit', 'dvda', 'dyke', 'eat my ass', 'ecchi', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'erotic', 'erotism', 'escort', 'eunuch', 'f u c k', 'f u c k e r', 'f_u_c_k', 'f4nny', 'fag', 'fagbag', 'fagfucker', 'fagging', 'faggit', 'faggitt', 'faggot', 'faggotcock', 'faggs', 'fagot', 'fagots', 'fags', 'fagtard', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'fecal', 'feck', 'fecker', 'felch', 'felching', 'fellate', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingerbang', 'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks', 'fingering', 'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks', 'fisting', 'flamer', 'flange', 'foah', 'fook', 'fooker', 'foot fetish', 'footjob', 'frotting', 'fuck', 'fuck buttons', 'fuck off', 'fucka', 'fuckass', 'fuckbag', 'fuckboy', 'fuckbrain', 'fuckbutt', 'fuckbutter', 'fucked', 'fucker', 'fuckers', 'fuckersucker', 'fuckface', 'fuckhead', 'fuckheads', 'fuckhole', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucknut', 'fucknutt', 'fuckoff', 'fucks', 'fuckstick', 'fucktard', 'fucktards', 'fucktart', 'fucktwat', 'fuckup', 'fuckwad', 'fuckwhit', 'fuckwit', 'fuckwitt', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'futanari', 'fux', 'fux0r', 'g-spot', 'gang bang', 'gangbang', 'gangbanged', 'gangbangs', 'gay', 'gay sex', 'gayass', 'gaybob', 'gaydo', 'gayfuck', 'gayfuckist', 'gaylord', 'gaysex', 'gaytard', 'gaywad', 'genitals', 'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'god damn', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'goddamnit', 'gokkun', 'golden shower', 'goo girl', 'gooch', 'goodpoop', 'gook', 'goregasm', 'gringo', 'grope', 'group sex', 'guido', 'guro', 'hand job', 'handjob', 'hard core', 'hard on', 'hardcore', 'hardcoresex', 'heeb', 'hell', 'hentai', 'heshe', 'ho', 'hoar', 'hoare', 'hoe', 'hoer', 'homo', 'homodumbshit', 'homoerotic', 'honkey', 'hooker', 'hore', 'horniest', 'horny', 'hot carl', 'hot chick', 'hotsex', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack Off', 'jack-off', 'jackass', 'jackoff', 'jaggi', 'jagoff', 'jail bait', 'jailbait', 'jap', 'jelly donut', 'jerk off', 'jerk-off', 'jerkass', 'jigaboo', 'jiggaboo', 'jiggerboo', 'jism', 'jiz', 'jizm', 'jizz', 'juggs', 'jungle bunny', 'junglebunny', 'kawk', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knob', 'knobbing', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kooch', 'kootch', 'kraut', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'kunja', 'kunt', 'kyke', 'l3i+ch', 'l3itch', 'labia', 'lameass', 'lardass', 'leather restraint', 'leather straight jacket', 'lemon party', 'lesbian', 'lesbo', 'lezzie', 'lmfao', 'lolita', 'lovemaking', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'make me come', 'male squirting', 'masochist', 'master-bate', 'masterb8', 'masterbat', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mcfagget', 'menage a trois', 'mick', 'milf', 'minge', 'missionary position', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'mound of venus', 'mr hands', 'muff', 'muff diver', 'muffdiver', 'muffdiving', 'munging', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nambla', 'nawashi', 'nazi', 'negro', 'neonazi', 'nig nog', 'nigaboo', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'niglet', 'nimphomania', 'nipple', 'nipples', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'nsfw images', 'nude', 'nudity', 'numbnuts', 'nut sack', 'nutsack', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'orgy', 'p0rn', 'paedophile', 'paki', 'panooch', 'panties', 'panty', 'pawn', 'pecker', 'peckerhead', 'pedobear', 'pedophile', 'pegging', 'penis', 'penisbanger', 'penisfucker', 'penispuffer', 'phone sex', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'piece of shit', 'pigfucker', 'pimpis', 'piss', 'piss pig', 'pissed', 'pissed off', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', 'pissing', 'pissoff', 'pisspig', 'playboy', 'pleasure chest', 'pole smoker', 'polesmoker', 'pollock', 'ponyplay', 'poof', 'poon', 'poonani', 'poonany', 'poontang', 'poop', 'poop chute', 'poopchute', 'poopuncher', 'porch monkey', 'porchmonkey', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', 'prince albert piercing', 'pron', 'pthc', 'pube', 'pubes', 'punanny', 'punany', 'punta', 'pusse', 'pussi', 'pussies', 'pussy', 'pussylicking', 'pussys', 'pust', 'puto', 'queaf', 'queef', 'queer', 'queerbait', 'queerhole', 'quim', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum', 'renob', 'retard', 'reverse cowgirl', 'rimjaw', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'ruski', 'rusty trombone', 's.o.b.', 's&m', 'sadism', 'sadist', 'sand nigger', 'sandler', 'sandnigger', 'sanger', 'santorum', 'scat', 'schlong', 'scissoring', 'screwing', 'scroat', 'scrote', 'scrotum', 'seks', 'semen', 'sex', 'sexo', 'sexy', 'shag', 'shagger', 'shaggin', 'shagging', 'shaved beaver', 'shaved pussy', 'shemale', 'shi+', 'shibari', 'shit', 'shitass', 'shitbag', 'shitbagger', 'shitblimp', 'shitbrains', 'shitbreath', 'shitcanned', 'shitcunt', 'shitdick', 'shite', 'shited', 'shitey', 'shitface', 'shitfaced', 'shitfuck', 'shitfull', 'shithead', 'shithole', 'shithouse', 'shiting', 'shitings', 'shits', 'shitspitter', 'shitstain', 'shitted', 'shitter', 'shitters', 'shittiest', 'shitting', 'shittings', 'shitty', 'shiz', 'shiznit', 'shota', 'shrimping', 'skank', 'skeet', 'skullfuck', 'slag', 'slanteye', 'slut', 'slutbag', 'sluts', 'smeg', 'smegma', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'son-of-a-bitch', 'spac', 'spic', 'spick', 'splooge', 'splooge moose', 'spooge', 'spook', 'spread legs', 'spunk', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'suckass', 'sucks', 'suicide girls', 'sultry women', 'swastika', 'swinger', 't1tt1e5', 't1tties', 'tainted love', 'tard', 'taste my', 'tea bagging', 'teets', 'teez', 'testical', 'testicle', 'threesome', 'throating', 'thundercunt', 'tied up', 'tight white', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'titty', 'tittyfuck', 'tittywank', 'titwank', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'turd', 'tushy', 'tw4t', 'twat', 'twathead', 'twatlips', 'twats', 'twatty', 'twatwaffle', 'twink', 'twinkie', 'two girls one cup', 'twunt', 'twunter', 'unclefucker', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'v14gra', 'v1gra', 'va-j-j', 'vag', 'vagina', 'vajayjay', 'venus mound', 'viagra', 'vibrator', 'violet wand', 'vjayjay', 'vorarephilia', 'voyeur', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wankjob', 'wanky', 'wet dream', 'wetback', 'white power', 'whoar', 'whore', 'whorebag', 'whoreface', 'willies', 'willy', 'wop', 'wrapping men', 'wrinkled starfish', 'xrated', 'xx', 'xxx', 'yaoi', 'yellow showers', 'yiffy', 'zoophilia', 'zubb', 'a$$', 'a$$hole', 'a55hole', 'ahole', 'anal impaler', 'anal leakage', 'analprobe', 'ass fuck', 'ass hole', 'assbang', 'assbanged', 'assbangs', 'assfaces', 'assh0le', 'beatch', 'bimbo', 'bitch tit', 'bitched', 'bloody hell', 'bootee', 'bootie', 'bull shit', 'bullshits', 'bullshitted', 'bullturds', 'bum boy', 'butt fuck', 'buttfuck', 'buttmunch', 'c-0-c-k', 'c-o-c-k', 'c-u-n-t', 'c.0.c.k', 'c.o.c.k.', 'c.u.n.t', 'caca', 'cacafuego', 'chi-chi man', 'child-fucker', 'clit licker', 'cock sucker', 'corksucker', 'corp whore', 'crackwhore', 'dammit', 'damned', 'damnit', 'darn', 'dick head', 'dick hole', 'dick shy', 'dick-ish', 'dickdipper', 'dickflipper', 'dickheads', 'dickish', 'f-u-c-k', 'f.u.c.k', 'fist fuck', 'fuck hole', 'fuck puppet', 'fuck trophy', 'fuck yo mama', 'fuck you', 'fuck-ass', 'fuck-bitch', 'fuck-tard', 'fuckedup', 'fuckmeat', 'fucknugget', 'fucktoy', 'fuq', 'gassy ass', 'h0m0', 'h0mo', 'ham flap', 'he-she', 'hircismus', 'holy shit', 'hom0', 'hoor', 'jackasses', 'jackhole', 'middle finger', 'moo foo', 'naked', 'p.u.s.s.y.', 'piss off', 'piss-off', 'rubbish', 's-o-b', 's0b', 'shit ass', 'shit fucker', 'shiteater', 'son of a bitch', 'son of a whore', 'two fingers', 'wh0re', 'wh0reface']
    for item in invalid_list:
        if item == string_to_analize:
            return True
    return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_code(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)

def verify_user(user: str, verified_input: int):
    try:
        found_user = users.query.filter_by(username=user).first()
        found_user.verified = verified_input
        db.session.commit()
        print("USER: " + user + " -> VERIFIED: " + verified_input)
    except:
        print("Could not complete this task.")

def match_security(session_type: str, match_id: str) -> bool: #this is for all of the control routes
    found_match = match.query.filter_by(_id=match_id).first()
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    user_verified = False
    with open("static/score_files/" + str(found_match._id) + ".json", "r") as file:
        file.seek(0)
        data = json.load(file)        
        print(found_user.username)

        if found_user != "" and found_user.username in data["shared_coaches"]:
            user_verified = True
    try:
        if 'coach' in session[session_type] and (found_match.created_by == session[session_type][0] or user_verified):
            return True
        else:
            return False
    except:
        return False

@app.route("/FAQ")
def FAQ():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("FAQ.html", data=found_user)

@app.route("/about")
def about():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("about.html", data=found_user)

@app.route("/termsofservice")
def termsofservice():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("termsofservice.html", data=found_user)

@app.route("/privacypolicy")
def privacypolicy():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("privacypolicy.html", data=found_user)

@app.route("/chooseprofilepicture")
def chooseprofilepicture():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("chooseprofilepic.html", data=found_user)
    else:
        return render_template("login.html")


@app.route("/newprofilepicture")
def newprofilepicture():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("profile-pic-animation.html", data=found_user)
    else:
        return render_template("login.html")

@app.route("/profile/edit")
def edit_profile():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("edit_profile.html", data=found_user)
    else:
        return render_template("login.html")

@app.route("/entering_match/<match_code>")
def entering_match(match_code):
    try:
        found_match = match.query.filter_by(match_code=match_code).first()
        try:
            found_user = users.query.filter_by(username=session['active_user'][0]).first()
        except:
            found_user = ""
        with open("static/score_files/" + str(found_match._id) + ".json", "r") as file:
            file.seek(0)
            data = json.load(file)
            try:
                if found_user != "" and found_user.username in data["shared_coaches"]:
                    return redirect(url_for("active_match_view", json_data_input=found_match._id))
            except:
                return render_template("player-or-spectator.html", data=found_user, match_data=found_match)
    except:
        return redirect(url_for("error", msg="Sorry, this match existed at one point. But the data has since been deleted."))
    return render_template("player-or-spectator.html", data=found_user, match_data=found_match)


@app.route("/joincode", methods=['POST', 'GET'])
def joincode():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    if request.method == 'POST':
        code_entry = request.form['code_entry']
        found_match = match.query.filter_by(match_code=code_entry).first()
        if found_match:
            if found_match.match_password == "":
                print('No password!')
                #route to live player dashboard
            return redirect(url_for('entering_match', match_code=found_match.match_code))
        return render_template("join_code_page.html", data="We can't find that match... Please check your join code and try again.")
    return render_template("join_code_page.html", data=None)

@app.route("/box_office/<match1>", methods=['GET', 'POST'])
def box_office(match1):
    match1 = match.query.filter_by(_id=match1).first()
    eventtype = (match1.event_type, match1.teams1.split("~"))
    if request.method == 'POST':
        password = request.form['password_entry']
        name = request.form['name_entry']
        if password == match1.match_password and not sanitize_inputs(name):
            if match1.event_type == 'Singles':
                tuple_data = (request.form['name_entry'], None)
            elif match1.event_type == 'Teams':
                tuple_data = (request.form['name_entry'], request.form['team_select'])
            try:
                Scoring.add_to_lobby(match1._id, tuple_data)
                session['active_player'] = name
            except:
                return redirect(url_forZ('error', msg="Sorry. This match is not yet live or there was a problem creating a live match file. Please check with your match administrator for more information."))
            return redirect(url_for('player_match_view', json_data_input=match1._id))
        else:
            return redirect(url_for("error", msg='Sorry. Your password was incorrect or your name was inapropriate. Please try again!'))
    return render_template('box_office.html', data=match1, data1=eventtype)

@app.route("/")
def index():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("index.html", data=found_user)

@app.route("/header", methods=['GET'])
def header():
    if 'active_user' in session:
        return render_template("header.html")
    return render_template("error.html", message="Sorry, you do not have access to this page.")

@app.route("/error/<msg>")
def error(msg):
    return render_template("error.html", message=msg)

@app.route("/login", methods=["POST", "GET"])
def login():
    found_user = ""
    if 'active_user' in session:
        return redirect(url_for('profile'))
    if request.method == "POST":

        username_input = request.form['username']
        password_input = request.form['password']
        found_user = users.query.filter_by(username=username_input).first()
        

        if found_user and found_user.username == username_input and found_user.password == hashingalg.hashPassword(password_input):
            session['active_user'] = [found_user.username, found_user.name, found_user.rank]
            found_user.last_login = datetime.now()
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            return render_template("login.html", data=found_user, message="Username and password were incorrect! Please try again.")

    return render_template("login.html", data=found_user)

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    logged_in_user = found_user
    date_year = str(found_user.first_login)
    date_year = date_year[0:4]

    date = datetime.strptime(str(found_user.first_login), "%Y-%m-%d %H:%M:%S.%f")
    month_index = date.month

    list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_name = list_of_months[month_index-1]

    #chooses three random users
    count = users.query.count()
    random_offset = randint(0, count - 1)
    random_offset2 = randint(0, count - 1)
    random_offset3 = randint(0, count - 1)
    random_user_one = users.query.offset(random_offset).limit(1).first()
    random_user_two = users.query.offset(random_offset2).limit(1).first()
    random_user_three = users.query.offset(random_offset3).limit(1).first()
    while (random_user_one._id == logged_in_user._id):
        random_offset = randint(0, count - 1)
        random_user_one = users.query.offset(random_offset).limit(1).first() 
    while (random_user_two._id == random_user_one._id or random_user_two._id == logged_in_user._id):
        random_offset2 = randint(0, count - 1)
        random_user_two = users.query.offset(random_offset2).limit(1).first() 
    while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id or random_user_three._id == logged_in_user._id):
        random_offset3 = randint(0, count - 1)
        random_user_three = users.query.offset(random_offset3).limit(1).first() 
    random_users_list = [random_user_one, random_user_two, random_user_three]

    #find recent matches
    recent_matches = match_archive.query.filter_by(username=session['active_user'][0]).all()
    recent_matches = [(get_archived_match(thing.filename), thing.date_added) for thing in recent_matches]
    recent_matches = recent_matches[::-1]
    print(recent_matches)

    if 'active_user' in session:
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                    return redirect(url_for('error', msg="Sorry, you have input an inapropriate or non-existant value. Please try again."))

            found_user.team = request.form['team']
            found_user.name = request.form['name']
            found_user.bio = request.form['bio']
            


            db.session.commit()

        return render_template("profile.html", month = month_name, random_users_list=random_users_list, recent_matches=recent_matches, year=date_year, data=found_user)
    return redirect(url_for('error', msg="You must login to access this page."))

@app.route("/profile/<user>", methods=['GET', 'POST'])
def get_user_profile(user):
    try:
        found_user = users.query.filter_by(username=user).first()
        date_year = str(found_user.first_login)
        date_year = date_year[0:4]

        date = datetime.strptime(str(found_user.first_login), "%Y-%m-%d %H:%M:%S.%f")
        month_index = date.month

        list_of_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_name = list_of_months[month_index-1]
    except:
        return redirect(url_for('error', msg="Sorry, that user does not exist."))
    
    #find recent matches
    recent_matches = match_archive.query.filter_by(username=user).all()
    recent_matches = [(get_archived_match(thing.filename), thing.date_added) for thing in recent_matches]
    recent_matches = recent_matches[::-1]
    
    try:
        logged_in_user = users.query.filter_by(username=session['active_user'][0]).first()
        print(logged_in_user.name)
        if logged_in_user.username == user:
            return redirect(url_for('profile'))
        else:
            #chooses three random users
            count = users.query.count()
            random_offset = randint(0, count - 1)
            random_offset2 = randint(0, count - 1)
            random_offset3 = randint(0, count - 1)
            random_user_one = users.query.offset(random_offset).limit(1).first()
            random_user_two = users.query.offset(random_offset2).limit(1).first()
            random_user_three = users.query.offset(random_offset3).limit(1).first()
            while (random_user_one._id == logged_in_user._id):
                random_offset = randint(0, count - 1)
                random_user_one = users.query.offset(random_offset).limit(1).first() 
            while (random_user_two._id == random_user_one._id or random_user_two._id == logged_in_user._id):
                random_offset2 = randint(0, count - 1)
                random_user_two = users.query.offset(random_offset2).limit(1).first() 
            while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id or random_user_three._id == logged_in_user._id):
                random_offset3 = randint(0, count - 1)
                random_user_three = users.query.offset(random_offset3).limit(1).first() 
            random_users_list = [random_user_one, random_user_two, random_user_three]
    except:
        logged_in_user = None
        count = users.query.count()
        random_offset = randint(0, count - 1)
        random_offset2 = randint(0, count - 1)
        random_offset3 = randint(0, count - 1)
        random_user_one = users.query.offset(random_offset).limit(1).first()
        random_user_two = users.query.offset(random_offset2).limit(1).first()
        random_user_three = users.query.offset(random_offset3).limit(1).first()
        while (random_user_two._id == random_user_one._id):
            random_offset2 = randint(0, count - 1)
            random_user_two = users.query.offset(random_offset2).limit(1).first() 
        while (random_user_three._id == random_user_one._id or random_user_three._id == random_user_two._id):
            random_offset3 = randint(0, count - 1)
            random_user_three = users.query.offset(random_offset3).limit(1).first() 
        random_users_list = [random_user_one, random_user_two, random_user_three]

    return render_template("user_profile_page.html", month = month_name, recent_matches=recent_matches, year=date_year, random_users_list=random_users_list, data1=found_user, data=logged_in_user)

@app.route("/create_round", methods=['GET', 'POST'])
def create_round():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
    if 'active_user' in session and session['active_user'][2] == "player":
        if request.method == "POST":
            try:
                new_match = match(request.form['matchname'], request.form['coursename'], request.form['starttime'], request.form['endtime'], ezfix, request.form['matchname'], generate_code(6), request.form['matchpassword'], request.form['eventtype'], request.form['matchtype'], request.form['numberofplayers'], session['active_user'][0], False)
                db.session.add(new_match)
                db.session.commit()
            except Exception as err:
                print(err)
                return redirect(url_for('error', msg="There was an error in creating your match."))

            return redirect(url_for('dashboard'))
        return render_template('create_round.html', course_data=found_course, data=found_user)
    return redirect(url_for('error', msg='You do not have access to this page.'))

@app.route("/create_match", methods=['GET', 'POST'])
def create_match():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
    if 'active_user' in session and session['active_user'][2] == "coach":
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                        break
                        return render_template('create_match.html', message="You have inputed an invalid value or an inapropriate value.")
            
            ezfix = request.form["hometeam"] + '~' + request.form["awayteam"]
            

            try:
                new_match = match(request.form['matchname'], request.form['coursename'], request.form['starttime'], request.form['endtime'], ezfix, request.form['matchname'], generate_code(6), request.form['matchpassword'], request.form['eventtype'], request.form['matchtype'], request.form['numberofplayers'], session['active_user'][0], False)
                db.session.add(new_match)
                db.session.commit()
            except Exception as err:
                print(err)
                return redirect(url_for('error', msg="There was an error in creating your match."))

            return redirect(url_for('dashboard'))
        
        return render_template('create_match.html', course_data=found_course, data=found_user)
    return redirect(url_for('error', msg='You do not have access to this page.'))

@app.route("/create_account/email_verification/resend_email/<email>")
def resend_email(email):
    with open('tokens.json', "r+") as file:
        data = json.load(file)
        target_email = email

        #gets key from email value
        for key, value in data.items():
            if isinstance(value, list) and target_email in value:
                target_key = key
                break

        username = data[target_key][1]

        new_key = emails1.send_validation_email(email, username)
        #renames key to new_key
        if target_key in data:
            data[new_key] = data.pop(target_key)

        file.seek(0, 0)
        json.dump(data, file, indent=3)
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("email_verification.html", data=found_user, email=email)

@app.route("/create_account/email_verification/<email>", methods=["POST", "GET"])
def email_verification(email):
    if request.method == 'POST':
        form_token = request.form['token_input']
        with open("tokens.json", "r+") as file:
            data = json.load(file)
            if form_token in data:
                new_user = users(
                    data[form_token][0],
                    data[form_token][1],
                    data[form_token][2],
                    data[form_token][3],
                    data[form_token][4],
                    data[form_token][5],
                    data[form_token][6],
                    data[form_token][7],
                    data[form_token][8],
                    data[form_token][9],
                    data[form_token][10],
                    datetime.strptime(data[form_token][11], "%Y-%m-%d %H:%M:%S.%f"),
                    datetime.strptime(data[form_token][11], "%Y-%m-%d %H:%M:%S.%f")
                )
                db.session.add(new_user)
                db.session.commit()
                new_username = data[form_token][1]
                new_rank = data[form_token][4]
                new_name = data[form_token][0]
                found_user = users.query.filter_by(username=new_username).first()
        
                session['active_user'] = [new_username, new_name, new_rank]
                del data[form_token]
                file.seek(0, 0)
                json.dump(data, file, indent=3)
                file.truncate()
            #might need a else statement here
        return redirect(url_for('chooseprofilepicture'))
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("email_verification.html", data=found_user, email=email)




@app.route("/reset_password/<email>/<name>")
def reset_password(email, name):
    with open('tokens.json', "r+") as file:
        data = json.load(file)
        data[emails1.send_reset_password_email(email, name)] = [email, name]
        file.seek(0, 0)
        json.dump(data, file, indent=3)
    return redirect(url_for('password_reset2', email=email))

@app.route("/password_reset2/<email>", methods=["POST", "GET"])
def password_reset2(email):
    found_user = ""
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    if request.method == "POST":
        form_token = request.form['token-input']
        with open("tokens.json", "r+") as file:
            data = json.load(file)
            if form_token in data:

                try:
                    found_user = users.query.filter_by(email=email).first()
                    found_user.password = hashingalg.hashPassword(request.form['new-password-input'])
                    db.session.commit()
                except:
                    return redirect(url_for("error", msg="Your account was not found. Please try again or contact support@bigblue.golf."))

                del data[form_token]
                file.seek(0, 0)
                json.dump(data, file, indent=3)
                file.truncate()
                return redirect(url_for('password_changed'))
            else:
                return render_template("reset_password.html", data=found_user, email=email, message="Invalid Token. Please verify the token you entered matches the one emailed to you. If there an issue, contact support at support@bigblue.golf.")
    else:
        return render_template("reset_password.html", data=found_user, message="We have sent a reset password token to your email.", email=email)

@app.route("/resend_password_reset_email/<email>")
def resend_password_email(email):
    found_user = ""
    with open('tokens.json', "r+") as file:
        data = json.load(file)
        target_email = email
    
        #gets token from email value
        for token, value in data.items():
            if isinstance(value, list) and target_email in value:
                target_token = token
                break

        #sets username to value listed under the target_key (token)
        username = ""
        try:
            username = data[target_token][1]
        except:
            return render_template("reset_password.html", data=found_user, email=email, message="Something went wrong. Please verify the token you entered matches the one emailed to you. If there an issue, contact support at support@bigblue.golf.")


        new_token = emails1.send_reset_password_email(email, username)

        #renames token to new_token
        if target_token in data:
            data[new_token] = data.pop(target_token)
        
        file.seek(0, 0)
        json.dump(data, file, indent=3)

    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("reset_password.html", data=found_user, email=email)


@app.route("/forgot_password")
def forgot_password():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("forgot_password.html", data=found_user)

@app.route("/reset_password_with_username/<user>", methods=["POST", "GET"])
def reset_password_with_username(user):
    #get the user's email from the username IMPORTANT
    found_user = ""
    found_email = ""
    try:
        found_user = users.query.filter_by(username=user).first()
        found_email = found_user.email
    except:
        found_user = ""
        return render_template("forgot_password.html", data=found_user, message="Username not found.")
    
    found_email = found_user.email

    print(found_email)
    return redirect(url_for('reset_password', email=found_email, name=user))
    



@app.route("/password_changed")
def password_changed():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    return render_template("password_change_successful.html", data=found_user)


@app.route("/edit_match/<match_to_edit>", methods=["POST", "GET"])
def edit_match(match_to_edit):
    found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
    found_match = match.query.filter_by(_id=match_to_edit).first()
    if found_match.match_live == 1:
        return redirect(url_for('error', msg="You cannot edit match details of matches that are live!"))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method == "POST":
            for item in request.form:
                if request.form[item] == "" or sanitize_inputs(request.form[item]):
                    if request.form["eventtype"] != "singles" and request.form["hometeam"] == "" and request.form["awayteam"] == "":
                        break
                    return render_template('edit_match.html', data=found_user, message="You have inputed an invalid value or an inapropriate value.", editing=found_match)
            
            ezfix = request.form["hometeam"] + '~' + request.form["awayteam"]

            try:
                found_match.event_type = request.form['eventtype']
                found_match.match_type = request.form['matchtype']
                found_match.teams1 = ezfix
                found_match.total_players = request.form['numberofplayers']
                found_match.match_name = request.form['matchname']
                found_match.match_course = request.form['coursename']

                print(request.form['coursename'])
                found_match.start_time = request.form['starttime']
                found_match.end_time = request.form['endtime']
                found_match.match_password = request.form['matchpassword']
                db.session.commit()
                print(found_match.teams1)
            except:
                redirect(url_for('error', msg="There was a problem adding your match to the database. Please make sure you have inputed all fields. If all else fails, contact customer suport."))
            
            return redirect(url_for("dashboard"))

        return render_template('edit_match.html', course_data=found_course, data=found_user, editing=found_match)

    return render_template("error", msg="You do not have access to this site!")


@app.route("/add_shared_coach/<filename>/<coach>")
def add_shared_coach_route(filename, coach):
    found_match = match.query.filter_by(_id=filename).first()
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    if 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        Scoring.add_shared_coach(filename, coach)
        coach_user = users.query.filter_by(username=coach).first()
        coach_email = coach_user.email
        print(coach_email)
        emails1.send_email(coach_email, ("@" + str(found_user.username) + " Shared a Match with you!"), ("User @" + str(found_user.username) + " shared a a match titled '" + str(found_match.match_name) + "' with you. This means you can help them manage and edit the match live. \n\nTo access the match's dashboard, you must be logged in, and then enter this join code: " + str(found_match.match_code) + " at https://bigblue.golf/joincode. \n\nThe Bigblue.golf Team\nFort Wayne, Indiana"))
        return redirect(url_for("active_match_view", json_data_input=found_match._id))
    return redirect(url_for('error', msg="You do not have permission to add coaches to this match."))

@app.route("/remove_shared_coach/<filename>/<coach>")
def remove_shared_coach_route(filename, coach):
    found_match = match.query.filter_by(_id=filename).first()
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    if 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        Scoring.remove_shared_coach(filename, coach)
        return redirect(url_for("active_match_view", json_data_input=found_match._id))
    return redirect(url_for('error', msg="You do not have permission to add coaches to this match."))


@app.route("/edit_course/<course_to_edit>", methods=["POST", "GET"])
def edit_course(course_to_edit):
    found_course = course.query.filter_by(_id=course_to_edit).first()
    if 'active_user' in session and session['active_user'][0] == found_course.created_by:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method == "POST":
            found_course.course_name = request.form['course-name']
            found_course.course_holes = request.form['numberholes']
            found_course.course_rating = request.form['course_rating']
            found_course.slope_rating = request.form['slope_rating']
            found_course.par1 = request.form['holepar1']
            found_course.par2 = request.form['holepar2']
            found_course.par3 = request.form['holepar3']
            found_course.par4 = request.form['holepar4']
            found_course.par5 = request.form['holepar5']
            found_course.par6 = request.form['holepar6']
            found_course.par7 = request.form['holepar7']
            found_course.par8 = request.form['holepar8']
            found_course.par9 = request.form['holepar9']
            found_course.par10 = request.form['holepar10']
            found_course.par11 = request.form['holepar11']
            found_course.par12 = request.form['holepar12']
            found_course.par13 = request.form['holepar13']
            found_course.par14 = request.form['holepar14']
            found_course.par15 = request.form['holepar15']
            found_course.par16 = request.form['holepar16']
            found_course.par17 = request.form['holepar17']
            found_course.par18 = request.form['holepar18']
            found_course.handicap1 = request.form['handicap_one']
            found_course.handicap2 = request.form['handicap_two']
            found_course.handicap3 = request.form['handicap_three']
            found_course.handicap4 = request.form['handicap_four']
            found_course.handicap5 = request.form['handicap_five']
            found_course.handicap6 = request.form['handicap_six']
            found_course.handicap7 = request.form['handicap_seven']
            found_course.handicap8 = request.form['handicap_eight']
            found_course.handicap9 = request.form['handicap_nine']
            found_course.handicap10 = request.form['handicap_ten']
            found_course.handicap11 = request.form['handicap_eleven']
            found_course.handicap12 = request.form['handicap_twelve']
            found_course.handicap13 = request.form['handicap_thirteen']
            found_course.handicap14 = request.form['handicap_fourteen']
            found_course.handicap15 = request.form['handicap_fifteen']
            found_course.handicap16 = request.form['handicap_sixteen']
            found_course.handicap17 = request.form['handicap_seventeen']
            found_course.handicap18 = request.form['handicap_eighteen']
            found_course.city = request.form['city']
            found_course.bio = ""
        
            db.session.commit()

            return redirect(url_for("course_dashboard"))
    
    return render_template('edit_course.html', data=found_user, editing=found_course)


@app.route("/delete_match/<match_to_delete>")
def delete_match(match_to_delete):
    found_match = match.query.filter_by(_id=match_to_delete).first()
    if found_match.match_live == 1:
        return redirect(url_for('error', msg="You cannot delete matches that are live!"))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][2] == "coach":
        #removes json file
        try:
            filename = str(found_match._id) + ".json"
            os.remove(os.path.join(app.config['SCORING_FOLDER'], str(filename)))
            #removes match from DB
            db.session.delete(found_match)
            db.session.commit()
            return redirect(url_for("dashboard"))
        except:
            db.session.delete(found_match)
            db.session.commit()
            return redirect(url_for("dashboard"))
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/delete_course/<course_to_delete>")
def delete_course(course_to_delete):
    found_course = course.query.filter_by(_id=course_to_delete).first()
    if 'active_user' in session and session['active_user'][0] == found_course.created_by:
        db.session.delete(found_course)
        db.session.commit()
        return redirect(url_for("course_dashboard"))
    return redirect(url_for('error', msg="You do not have access to this page."))

@app.route("/create_account", methods=['POST', 'GET'])
def create_account():
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    if request.method == "POST":
        for item in request.form:
            if request.form[item] == "" or sanitize_inputs(request.form[item]):
                return redirect(url_for('error', msg="Your value was either blank or inapropriate. Please input all correct values. The problem is with the field: [add go back code]" + request.form[item]))
        found_username = users.query.filter_by(username=request.form['username']).first()
        found_email = users.query.filter_by(email=request.form['email']).first()
        if found_username or found_email:
            return render_template('create_account.html', message="Sorry, the email or username you entered is already in use.", data=found_user)
        
        today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        password = hashingalg.hashPassword(request.form['password'])
        with open('tokens.json', "r+") as file:
            data = json.load(file)
            data[emails1.send_validation_email(request.form['email'], request.form['username'])] = [request.form['name'], request.form['username'], password, request.form['email'], request.form['rank'], request.form['gender'], request.form['bio'], request.form['team'], 0, "defaultprofilepicture.png", "BigBluebanner.png", str(today_date), str(today_date)]
            file.seek(0, 0)
            json.dump(data, file, indent=3)
        return redirect(url_for('email_verification', email=request.form['email']))
    return render_template('create_account.html', data=found_user)

@app.route("/delete_account")
def delete_account():

    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    db.session.delete(found_user)
    db.session.commit()

    session.pop('active_user')

    return redirect(url_for('index'))

@app.route("/edit_user_profile", methods=["POST"])
def edit_user_profile():
    if request.method == "POST" and 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        found_user.team = request.form['team']
        found_user.name = request.form['name']
        found_user.bio = request.form['bio']
        found_user.email = request.form['email']

        db.session.commit()

        return redirect(url_for("profile"))
    return redirect(url_for('error', msg="Something went wrong. Please try again!"))


@app.route("/choose_banner", methods=["POST"])
def choose_banner():
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    if request.method == "POST" and 'active_user' in session:
        found_user.banner = request.form['banner']
        db.session.commit()

        return redirect(url_for("profile"))
    return redirect(url_for('error', msg="Something went wrong. Please try again!"))


@app.route("/upload_profile_pic", methods=["POST"])
def upload_profile_pic():
    if request.method == "POST" and 'active_user' in session:
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(url_for('error', msg="Sorry, you did not upload an image file. Please try again!"))
        file = request.files['file']
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '' or sanitize_inputs(file.filename):
            return redirect(url_for("error", msg="Sorry, your file did not have a name. Please try again."))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return redirect(url_for("error", msg="Sorry, there was a problem uploading your file. You might need to contact customer support!"))

        if filename == found_user.pic:
                    return redirect(url_for('newprofilepicture'))

        if found_user.pic != 'defaultprofilepicture.png':
            try:
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], found_user.pic))
            except:
                found_user.pic = filename        
        found_user.pic = filename
        db.session.commit()

        return redirect(url_for('newprofilepicture'))
    
    return redirect(url_for('error', msg="You do not have access to this site"))

@app.route("/logout")
def logout():
    if 'active_user' in session: 
        session.pop('active_user')
        return redirect(url_for('index'))
    return redirect(url_for('error', msg="How can you log out... if you are not logged in?"))

@app.route("/admin/<password>")
def admin(password):
    if password == "aW1wdmVyc3VzZHdhcmY":
        return render_template("admin.html")
    else:
        return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/admin/send_email_notification/<password>", methods=['POST'])
def send_email_notification(password):
    if password == 'graysonisthebestcomposer':
        conn = sqlite3.connect('instance/webdata.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''SELECT * from USERS''')
        result = cursor.fetchall()
        for user in result:
            print("Email sent to: " + user[4])
            try:
                emails1.send_email(user[4], 'Update from BigBlue.golf', request.form['content'])
            except:
                print("Could not sent email to " + user[4])
            print('___' + request.form['content'])
        return render_template("admin.html", message="Messages sent sucsessfuly!")
    else:
        return render_template("admin.html", message="Password was incorrect!")

@app.route("/dashboard")
def dashboard():
    if 'active_user' in session and session['active_user'][2]:
        found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
        found_match = match.query.filter_by(created_by=session['active_user'][0]).all()
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("dashboard.html", course_data=found_course, data=found_user, match_data=found_match)
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route("/course_dashboard")
def course_dashboard():
    if 'active_user' in session:
        found_course = course.query.filter_by(created_by=session['active_user'][0]).all()
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        return render_template("course_dashboard.html", data=found_user, course_data=found_course)
    return redirect(url_for('error', msg="You do not have access to this site."))

@app.route('/start_match/<match_id>/<course_id>')
def start_match(match_id, course_id):
    found_match = match.query.filter_by(_id=match_id).first()
    found_course = course.query.filter_by(_id=course_id).first()
    found_user = users.query.filter_by(username=session['active_user'][0]).first()
    print(session['active_user'][0], found_match.created_by)
    if found_match.match_live == 1:
        return redirect(url_for('error', data=found_user, msg='This match has already started. Try refreshing your match dashboard to gain access.'))
    elif found_match.match_live == 2:
         return redirect(url_for('error', data=found_user, msg='This match has finished. Try creating another match.'))
    elif 'active_user' in session and session['active_user'][0] == found_match.created_by and session['active_user'][0] == found_course.created_by:
        #match_live is updated in database, from 0 (not live) to 1 (live)
        found_match.match_live = 1
        db.session.commit()

        #creates json
        Scoring.create_json(
            found_match._id, 
            found_match.match_code,
            found_match.match_password,
            found_course.course_holes, 
            found_match.match_name, 
            found_match.start_time, 
            found_match.end_time, 
            found_match.teams1.split("~")[0], 
            found_match.teams1.split("~")[1], 
            found_match.event_type, 
            found_match.match_type,
            found_match._id,
            found_course.par1,
            found_course.par2,
            found_course.par3,
            found_course.par4,
            found_course.par5,
            found_course.par6,
            found_course.par7,
            found_course.par8,
            found_course.par9,
            found_course.par10,
            found_course.par11,
            found_course.par12,
            found_course.par13,
            found_course.par14,
            found_course.par15,
            found_course.par16,
            found_course.par17,
            found_course.par18

        )
        return redirect(url_for("active_match_view", json_data_input=found_match._id))
    else:
        return redirect(url_for('error', data=found_user, msg='You do not have access to this site.'))
    
   

@app.route("/return_user_data/<password>", methods=['GET'])
def return_user_data(password):
    print("hi")
    if password == "123":
        return return_admin_data()
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

@app.route("/change_verified_status/<admin>/<user>/<verified>")
def change_verified_status(admin, user, verified):
    if admin == '123':
        verify_user(user, verified)
        return 'USER: ' + user + " verification status has changed!",200
    else:
        return 'Sorry, you do not have access to this site.'

@app.route("/spectator_match_view/<json_data_input>")
def spectator_match_view(json_data_input):
    scores = []
    try:
        found_match = match.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        found_match_owner = users.query.filter_by(username=match_owner).first()
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
    except:
        try:
            found_match = match_archive.query.filter_by(_id=json_data_input).first()
            match_owner = found_match.created_by
            match_date = found_match.start_time
            found_match_owner = users.query.filter_by(username=match_owner).first()
            match_course = found_match.match_course
            found_course = course.query.filter_by(created_by=match_owner).first()
            match_location = found_course.city
        except:
            return redirect(url_for('error', msg='This match does not exist!'))
    try:
        json_data = Scoring.return_data(json_data_input)
        try:
            found_user = users.query.filter_by(username=session['active_user'][0]).first()
            if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
            else:
                scores = Scoring.calc_match_results(json_data['match_info']['id'])
        except:
            found_user = ''
            if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
            else:
                scores = Scoring.calc_match_results(json_data['match_info']['id'])
        return render_template("spectator-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data = scores)
    except:
        try:
            json_data = Scoring.return_archive_data(json_data_input)
            try:
                found_user = users.query.filter_by(username=session['active_user'][0]).first()
                if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                else:
                    scores = Scoring.calc_match_results(json_data['match_info']['id'])
            except:
                found_user = ''
                if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
                    scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                else:
                    scores = Scoring.calc_match_results(json_data['match_info']['id'])
            return render_template("spectator-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data = scores)
        except:
            return redirect(url_for('error', msg='This match does not exist!'))


@app.route("/player_match_view/<json_data_input>", methods=['GET', 'POST'])
def player_match_view(json_data_input):
    if 'active_player' in session:
        json_data = None
        try:
            found_match = match.query.filter_by(_id=json_data_input).first()
            match_owner = found_match.created_by
            match_date = found_match.start_time
            found_match_owner = users.query.filter_by(username=match_owner).first()
            match_course = found_match.match_course
            found_course = course.query.filter_by(created_by=match_owner).first()
            match_location = found_course.city
        except:
            found_match = match_archive.query.filter_by(_id=json_data_input).first()
            match_owner = found_match.created_by
            match_date = found_match.start_time
            found_match_owner = users.query.filter_by(username=match_owner).first()
            match_course = found_match.match_course
            found_course = course.query.filter_by(created_by=match_owner).first()
            match_location = found_course.city
        try:
            json_data = Scoring.return_data(json_data_input)
        except:
            return redirect(url_for('error', msg='This match is not yet live.'))

        
        if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
            try:
                scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
                json_data = Scoring.return_data(json_data_input)
                print(scores)
            except:
                json_data = Scoring.return_data(json_data_input)
        else:
            scores = Scoring.calc_match_results(json_data['match_info']['id'])
        
        

        try:
            found_user = users.query.filter_by(username=session['active_user'][0]).first()
        except:
            found_user = ''
        if request.method =="POST":
            return redirect(url_for("player_match_view", date=match_date, course=match_course, city=match_location, data1=found_match_owner, active_player=session['active_player'], json_data_input = json_data['match_info']['id']))
        return render_template("player-active-match-view.html", date=match_date, course=match_course, city=match_location, data1=found_match_owner, active_player=session['active_player'], data=found_user, playerdata=json_data, scoring_data = scores)
    else:
        return redirect(url_for('error', msg='You do not have access to this site until you join a match.'))
    
@app.route("/active_match_view/<json_data_input>")
def active_match_view(json_data_input):
    json_data = None
    try:
        found_match = match.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        found_match_owner = users.query.filter_by(username=match_owner).first()
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
    except:
        found_match = match_archive.query.filter_by(_id=json_data_input).first()
        match_owner = found_match.created_by
        match_date = found_match.start_time
        found_match_owner = users.query.filter_by(username=match_owner).first()
        match_course = found_match.match_course
        found_course = course.query.filter_by(created_by=match_owner).first()
        match_location = found_course.city
    try:
        json_data = Scoring.return_data(json_data_input)
    except:
        return redirect(url_for('error', msg='This match is not yet live.'))
    scores = []
    found_user=''
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ''

    if json_data['match_info']['gamemode'] == 'Match Play' and json_data['match_info']['match_type'] == 'Teams':
        scores = Scoring.calc_match_play_results(json_data['match_info']['id'])
        players_used = []
        for player in json_data["players"]:
            try:
                opponent = json_data["players"][player]["opponent"]
                players_used.append(player)
                players_used.append(opponent)
            except:
                continue
        

    elif json_data['match_info']['gamemode'] == 'Stroke Play' and json_data['match_info']['match_type'] == 'Teams':
        scores = Scoring.calc_match_results(json_data['match_info']['id'])

    if match_security('active_user', json_data_input):
        return render_template("active_match_view.html", json_data_input=json_data_input, date=match_date, course=match_course, city=match_location, data1=found_match_owner, data=found_user, playerdata=json_data, scoring_data=scores, rank=session['active_user'][2])
    else:
        return redirect(url_for('error', userdata=found_user, msg="You do not have access to this site!"))

@app.route("/create_course_new", methods=['GET', 'POST'])
def create_course_new():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method =="POST":

            if session['active_user'][2] == 'coach':

                return redirect(url_for("course_dashboard"))

            elif session['active_user'][2] == 'player':

                return redirect(url_for("course_dashboard"))

        return render_template("create_course_new.html", data=found_user)
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))


@app.route("/create_course", methods=['GET', 'POST'])
def create_course():
    if 'active_user' in session:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
        if request.method =="POST":

            if session['active_user'][2] == 'coach':

                for item in request.form:
                    if sanitize_inputs(item) or 'numberholes' not in request.form:
                        return render_template("create_course.html", message='Your values were either blank or inapropriate. Please try again.')


                course_entry = course(request.form["course-name"], request.form["numberholes"], 0.0, 0.0, request.form["holepar1"], '', request.form["holepar2"], '', request.form["holepar3"], '', request.form["holepar4"], '', request.form["holepar5"], '', request.form["holepar6"], '', request.form["holepar7"], '', request.form["holepar8"], '', request.form["holepar9"], '', request.form["holepar10"], '', request.form["holepar11"], '', request.form["holepar12"], '', request.form["holepar13"], '', request.form["holepar14"], '', request.form["holepar15"], '', request.form["holepar16"], '', request.form["holepar17"], '', request.form["holepar18"], '', request.form['city'], '', session['active_user'][0])
                db.session.add(course_entry)
                db.session.commit()
                found_course = course.query.filter_by(created_by=session['active_user'][0]).all()

                return redirect(url_for("course_dashboard"))

            elif session['active_user'][2] == 'player':

                for item in request.form:
                    if sanitize_inputs(item) or 'numberholes' not in request.form:
                        return render_template("create_course.html", message='Your values were either blank or inapropriate. Please try again.')


                course_entry = course(request.form["course-name"], request.form["numberholes"], request.form['course_rating'], request.form['slope_rating'], request.form["holepar1"], request.form['handicap_one'], request.form["holepar2"], request.form['handicap_two'], request.form["holepar3"], request.form['handicap_three'], request.form["holepar4"], request.form['handicap_four'], request.form["holepar5"], request.form['handicap_five'], request.form["holepar6"], request.form['handicap_six'], request.form["holepar7"], request.form['handicap_seven'], request.form["holepar8"], request.form['handicap_eight'], request.form["holepar9"], request.form['handicap_nine'], request.form["holepar10"], request.form['handicap_ten'], request.form["holepar11"], request.form['handicap_eleven'], request.form["holepar12"], request.form['handicap_twelve'], request.form["holepar13"], request.form['handicap_thirteen'], request.form["holepar14"], request.form['handicap_fourteen'], request.form["holepar15"], request.form['handicap_fifteen'], request.form["holepar16"], request.form['handicap_sixteen'], request.form["holepar17"], request.form['handicap_seventeen'], request.form["holepar18"], request.form['handicap_eighteen'], request.form['city'], '', session['active_user'][0])
                db.session.add(course_entry)
                db.session.commit()
                found_course = course.query.filter_by(created_by=session['active_user'][0]).all()

                return redirect(url_for("course_dashboard"))

        return render_template("create_course.html", data=found_user)
    else:
        return redirect(url_for("error", msg='Sorry, you do not have access to this site.'))

@app.route("/change_message/<filename>/<message>")
def change_message(filename, message):
    if match_security('active_user', filename):
        Scoring.change_message(filename, message)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/kick_player/<filename>/<player>", methods=['GET', 'POST'])
def kick_player(filename, player):
    if match_security('active_user', filename):
        player = player.replace("%20", " ")
        Scoring.kick_player(filename, player)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/add_player/<filename>/<team>/<player_name>", methods=['GET', 'POST'])
def add_player(filename, team, player_name):
    if match_security('active_user', filename):
        Scoring.add_player(filename, team, player_name)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/edit_score/<filename>/<player>/<hole>/<new_score>")
def edit_score(filename, player, hole, new_score):
    if match_security('active_user', filename) or session['active_player']: #check if this is player
        try:
            new_score = re.sub('[^\d]', '', new_score)
            Scoring.edit_score(filename, player, hole, new_score)
        except:
            return redirect(url_for('error', msg='Please input a vaild value. Integers are required.'))
        if "active_user" in session:
            return redirect(url_for("active_match_view", json_data_input=filename))
        elif "active_player" in session:
            return redirect(url_for("player_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/end_match/<filename>")
def end_match(filename):
    #TODO: ARCHIVE DATA
    if match_security('active_user', filename):
        try:
            del session['active_player']
        except:
            pass

        found_match = match.query.filter_by(_id=filename).first()
        found_match.match_live = 2

        current_time = datetime.now()
        new_entry = match_archive(session['active_user'][0], filename, current_time)
        db.session.add(new_entry)

        db.session.commit()

        archive_match(filename)
        os.remove('static/score_files/' + filename + '.json')

        return redirect(url_for("index"))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/change_opponent/<filename>/<player1>/<player2>")
def change_opponent(filename, player1, player2):
    if match_security('active_user', filename):
        Scoring.change_opponent(filename, player1, player2)
        return redirect(url_for("active_match_view", json_data_input=filename))
    else:
        return redirect(url_for("error", msg="You do not have access to this method!"))

@app.route("/calc_relation/<filename>/<player>", methods=["GET"])
def calc_relation(filename, player):
    preview = Scoring.calc_relation_to_par(filename, player)
    print(preview)
    return preview, 200

@app.route("/calc_match/<filename>/<player1>/<player2>", methods=["GET"])
def calc_match(filename, player1, player2):
    #try:
    preview = Scoring.calc_match_status(filename, player1, player2)
    print(preview)
    #except:
        #return redirect(url_for('error', msg="Please enter a integer."))
    return preview, 200

@app.route("/lowest_team_score/<filename>", methods=["GET"])
def lowest_team_score(filename):
    try:
        preview = Scoring.get_lowest_team_score(Scoring.get_team_scores(filename))
    except:
        return redirect(url_for('error', msg="There was an error in calculating the lowest team score."))

    if len(preview[0]) > 1:
        return_string = ', '.join(preview[0])
        return return_string, 200
    else:
        return preview[0][0]

@app.route("/search/<searchbar>", methods=["GET", "POST"])
def search(searchbar):
    found_user = ""
    try:
        found_user = users.query.filter_by(username=session['active_user'][0]).first()
    except:
        found_user = ""
    keyword = searchbar
    if (searchbar == ""):
        keyword = "404"
    search_query = db.session.query(users).filter(
        db.or_(
            users.username.like(f"%{keyword}%"),
            users.name.like(f"%{keyword}%")
        )).limit(100)
    return render_template("search_results.html", keyword=keyword, search_query=search_query, data=found_user)
    
@app.route("/golf_clap/<filename>/<player>")
def golf_clap(filename, player):
    #try:
    Scoring.add_golf_clap(filename, player)
    return 'Golf clap added to player: ' + player,200
    #except:
        #return 'Could not add golf clap to player: ' + player,500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, port=8000, debug=True)