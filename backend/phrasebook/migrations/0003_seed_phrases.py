from django.db import migrations


PHRASES = [
    {
        "slug": 'hello',
        "order": 0,
        "translations": {'en': 'Hello', 'es': 'Hola', 'fr': 'Bonjour', 'hi': 'नमस्ते', 'kn': 'ನಮಸ್ಕಾರ', 'ml': 'നമസ്കാരം', 'ta': 'வணக்கம்', 'te': 'నమస్కారం'},
        "translit": {'hi': ['namaste'], 'te': ['namaskaram']},
    },
    {
        "slug": 'how_are_you',
        "order": 1,
        "translations": {'en': 'How are you?', 'es': '¿Cómo estás?', 'fr': 'Comment ça va ?', 'hi': 'आप कैसे हैं?', 'kn': 'ನೀವು ಹೇಗಿದ್ದೀರಿ?', 'ml': 'സുഖമാണോ?', 'ta': 'நீங்கள் எப்படி இருக்கிறீர்கள்?', 'te': 'ఎలా వున్నారు?'},
        "translit": {'hi': ['aap kaise hain', 'kaise ho'], 'te': ['ela vunnaru', 'ela unnaru', 'yela vunnaru', 'elavunnaru']},
    },
    {
        "slug": 'good_morning',
        "order": 2,
        "translations": {'en': 'Good morning', 'es': 'Buenos días', 'fr': 'Bonjour', 'hi': 'सुप्रभात', 'kn': 'ಶುಭೋದಯ', 'ml': 'സുപ്രഭാതം', 'ta': 'காலை வணக்கம்', 'te': 'శుభోదయం'},
        "translit": {'hi': ['suprabhat'], 'te': ['shubhodayam']},
    },
    {
        "slug": 'good_night',
        "order": 3,
        "translations": {'en': 'Good night', 'es': 'Buenas noches', 'fr': 'Bonne nuit', 'hi': 'शुभ रात्रि', 'kn': 'ಶುಭ ರಾತ್ರಿ', 'ml': 'ശുഭരാത്രി', 'ta': 'இனிய இரவு', 'te': 'శుభరాత్రి'},
        "translit": {'hi': ['shubh ratri'], 'te': ['shubharatri']},
    },
    {
        "slug": 'thank_you',
        "order": 4,
        "translations": {'en': 'Thank you', 'es': 'Gracias', 'fr': 'Merci', 'hi': 'धन्यवाद', 'kn': 'ಧನ್ಯವಾದಗಳು', 'ml': 'നന്ദി', 'ta': 'நன்றி', 'te': 'ధన్యవాదాలు'},
        "translit": {'hi': ['dhanyavaad', 'shukriya'], 'te': ['dhanyavadalu']},
    },
    {
        "slug": 'please',
        "order": 5,
        "translations": {'en': 'Please', 'es': 'Por favor', 'fr': "S'il vous plaît", 'hi': 'कृपया', 'kn': 'ದಯವಿಟ್ಟು', 'ml': 'ദയവായി', 'ta': 'தயவுசெய்து', 'te': 'దయచేసి'},
        "translit": {'hi': ['kripya'], 'te': ['dayachesi']},
    },
    {
        "slug": 'yes',
        "order": 6,
        "translations": {'en': 'Yes', 'es': 'Sí', 'fr': 'Oui', 'hi': 'हाँ', 'kn': 'ಹೌದು', 'ml': 'അതെ', 'ta': 'ஆம்', 'te': 'అవును'},
        "translit": {'hi': ['haan'], 'te': ['avunu']},
    },
    {
        "slug": 'no',
        "order": 7,
        "translations": {'en': 'No', 'es': 'No', 'fr': 'Non', 'hi': 'नहीं', 'kn': 'ಇಲ್ಲ', 'ml': 'ഇല്ല', 'ta': 'இல்லை', 'te': 'కాదు'},
        "translit": {'hi': ['nahi', 'nahin'], 'te': ['kaadu', 'kadu']},
    },
    {
        "slug": 'sorry',
        "order": 8,
        "translations": {'en': 'Sorry', 'es': 'Lo siento', 'fr': 'Pardon', 'hi': 'माफ़ कीजिए', 'kn': 'ಕ್ಷಮಿಸಿ', 'ml': 'ക്ഷമിക്കണം', 'ta': 'மன்னிக்கவும்', 'te': 'క్షమించండి'},
        "translit": {'hi': ['maaf kijiye'], 'te': ['kshaminchandi']},
    },
    {
        "slug": 'whats_your_name',
        "order": 9,
        "translations": {'en': 'What is your name?', 'es': '¿Cómo te llamas?', 'fr': 'Comment vous appelez-vous ?', 'hi': 'आपका नाम क्या है?', 'kn': 'ನಿಮ್ಮ ಹೆಸರೇನು?', 'ml': 'നിന്റെ പേരെന്താണ്?', 'ta': 'உங்கள் பெயர் என்ன?', 'te': 'మీ పేరు ఏమిటి?'},
        "translit": {'hi': ['aapka naam kya hai'], 'te': ['mee peru emiti']},
    },
    {
        "slug": 'my_name_is',
        "order": 10,
        "translations": {'en': 'My name is', 'es': 'Me llamo', 'fr': "Je m'appelle", 'hi': 'मेरा नाम है', 'kn': 'ನನ್ನ ಹೆಸರು', 'ml': 'എന്റെ പേര്', 'ta': 'என் பெயர்', 'te': 'నా పేరు'},
        "translit": {'hi': ['mera naam hai'], 'te': ['naa peru']},
    },
    {
        "slug": 'where_are_you_from',
        "order": 11,
        "translations": {'en': 'Where are you from?', 'es': '¿De dónde eres?', 'fr': "D'où venez-vous ?", 'hi': 'आप कहाँ से हैं?', 'kn': 'ನೀವು ಎಲ್ಲಿಂದ ಬಂದಿದ್ದೀರಿ?', 'ml': 'നിങ്ങൾ എവിടെ നിന്നാണ്?', 'ta': 'நீங்கள் எங்கிருந்து வருகிறீர்கள்?', 'te': 'మీరు ఎక్కడ నుండి వచ్చారు?'},
        "translit": {'hi': ['aap kahan se hain'], 'te': ['meeru ekkada nundi vacharu']},
    },
    {
        "slug": 'i_am_fine',
        "order": 12,
        "translations": {'en': 'I am fine', 'es': 'Estoy bien', 'fr': 'Je vais bien', 'hi': 'मैं ठीक हूँ', 'kn': 'ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ', 'ml': 'എനിക്ക് സുഖമാണ്', 'ta': 'நான் நலமாக இருக்கிறேன்', 'te': 'నేను బాగున్నాను'},
        "translit": {'hi': ['main theek hoon', 'main thik hu'], 'te': ['nenu baagunnanu', 'nenu bagunnanu']},
    },
    {
        "slug": 'see_you_later',
        "order": 13,
        "translations": {'en': 'See you later', 'es': 'Nos vemos luego', 'fr': 'À plus tard', 'hi': 'बाद में मिलते हैं', 'kn': 'ನಂತರ ಸಿಗೋಣ', 'ml': 'പിന്നീട് കാണാം', 'ta': 'பின்னர் சந்திப்போம்', 'te': 'తర్వాత కలుద్దాం'},
        "translit": {'hi': ['baad mein milte hain'], 'te': ['tarvata kaluddam']},
    },
    {
        "slug": 'good_bye',
        "order": 14,
        "translations": {'en': 'Goodbye', 'es': 'Adiós', 'fr': 'Au revoir', 'hi': 'अलविदा', 'kn': 'ವಿದಾಯ', 'ml': 'വിട', 'ta': 'பிரியாவிடை', 'te': 'వీడ్కోలు'},
        "translit": {'hi': ['alvida'], 'te': ['veedkolu']},
    },
    {
        "slug": 'how_much',
        "order": 15,
        "translations": {'en': 'How much is this?', 'es': '¿Cuánto cuesta esto?', 'fr': 'Combien ça coûte ?', 'hi': 'यह कितने का है?', 'kn': 'ಇದು ಎಷ್ಟು?', 'ml': 'ഇതിന് എത്ര വില?', 'ta': 'இது எவ்வளவு?', 'te': 'ఇది ఎంత?'},
        "translit": {'hi': ['yah kitne ka hai'], 'te': ['idi entha']},
    },
    {
        "slug": 'where_is_bathroom',
        "order": 16,
        "translations": {'en': 'Where is the bathroom?', 'es': '¿Dónde está el baño?', 'fr': 'Où sont les toilettes ?', 'hi': 'शौचालय कहाँ है?', 'kn': 'ಶೌಚಾಲಯ ಎಲ್ಲಿದೆ?', 'ml': 'ശുചിമുറി എവിടെയാണ്?', 'ta': 'கழிப்பறை எங்கே?', 'te': 'బాత్రూమ్ ఎక్కడ ఉంది?'},
        "translit": {'hi': ['shauchalay kahan hai'], 'te': ['bathroom ekkada undi']},
    },
    {
        "slug": 'i_dont_understand',
        "order": 17,
        "translations": {'en': "I don't understand", 'es': 'No entiendo', 'fr': 'Je ne comprends pas', 'hi': 'मुझे समझ नहीं आया', 'kn': 'ನನಗೆ ಅರ್ಥವಾಗಲಿಲ್ಲ', 'ml': 'എനിക്ക് മനസ്സിലായില്ല', 'ta': 'எனக்கு புரியவில்லை', 'te': 'నాకు అర్థం కాలేదు'},
        "translit": {'hi': ['mujhe samajh nahin aaya'], 'te': ['naaku artham kaledu']},
    },
    {
        "slug": 'can_you_help_me',
        "order": 18,
        "translations": {'en': 'Can you help me?', 'es': '¿Puedes ayudarme?', 'fr': "Pouvez-vous m'aider ?", 'hi': 'क्या आप मेरी मदद कर सकते हैं?', 'kn': 'ನೀವು ನನಗೆ ಸಹಾಯ ಮಾಡಬಲ್ಲಿರಾ?', 'ml': 'നിങ്ങൾക്ക് എന്നെ സഹായിക്കാമോ?', 'ta': 'நீங்கள் எனக்கு உதவ முடியுமா?', 'te': 'మీరు నాకు సహాయం చేయగలరా?'},
        "translit": {'hi': ['kya aap meri madad kar sakte hain'], 'te': ['meeru naaku sahayam cheyagalara']},
    },
    {
        "slug": 'i_love_you',
        "order": 19,
        "translations": {'en': 'I love you', 'es': 'Te quiero', 'fr': "Je t'aime", 'hi': 'मैं तुमसे प्यार करता हूँ', 'kn': 'ನಾನು ನಿನ್ನನ್ನು ಪ್ರೀತಿಸುತ್ತೇನೆ', 'ml': 'ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു', 'ta': 'நான் உன்னை காதலிக்கிறேன்', 'te': 'నేను నిన్ను ప్రేమిస్తున్నాను'},
        "translit": {'hi': ['main tumse pyaar karta hoon'], 'te': ['nenu ninnu premisthunnanu']},
    },
    {
        "slug": 'water',
        "order": 20,
        "translations": {'en': 'Water', 'es': 'Agua', 'fr': 'Eau', 'hi': 'पानी', 'kn': 'ನೀರು', 'ml': 'വെള്ളം', 'ta': 'தண்ணீர்', 'te': 'నీళ్ళు'},
        "translit": {'hi': ['paani'], 'te': ['neellu']},
    },
    {
        "slug": 'food',
        "order": 21,
        "translations": {'en': 'Food', 'es': 'Comida', 'fr': 'Nourriture', 'hi': 'खाना', 'kn': 'ಆಹಾರ', 'ml': 'ഭക്ഷണം', 'ta': 'உணவு', 'te': 'ఆహారం'},
        "translit": {'hi': ['khaana'], 'te': ['aaharam']},
    },
    {
        "slug": 'what_time',
        "order": 22,
        "translations": {'en': 'What time is it?', 'es': '¿Qué hora es?', 'fr': 'Quelle heure est-il ?', 'hi': 'अभी क्या समय है?', 'kn': 'ಈಗ ಎಷ್ಟು ಗಂಟೆ?', 'ml': 'ഇപ്പോൾ എത്ര സമയമായി?', 'ta': 'இப்போது என்ன நேரம்?', 'te': 'సమయం ఎంత అయింది?'},
        "translit": {'hi': ['abhi kya samay hai'], 'te': ['samayam entha ayindi']},
    },
    {
        "slug": 'nice_to_meet_you',
        "order": 23,
        "translations": {'en': 'Nice to meet you', 'es': 'Mucho gusto', 'fr': 'Enchanté(e)', 'hi': 'आपसे मिलकर खुशी हुई', 'kn': 'ನಿಮ್ಮನ್ನು ಭೇಟಿಯಾಗಿ ಸಂತೋಷವಾಯಿತು', 'ml': 'നിങ്ങളെ കണ്ടതിൽ സന്തോഷം', 'ta': 'உங்களை சந்தித்ததில் மகிழ்ச்சி', 'te': 'మిమ్మల్ని కలవడం సంతోషంగా ఉంది'},
        "translit": {'hi': ['aapse milkar khushi hui'], 'te': ['mimmalni kalavadam santoshanga undi']},
    },
    {
        "slug": 'good_afternoon',
        "order": 24,
        "translations": {'en': 'Good afternoon', 'es': 'Buenas tardes', 'fr': 'Bon après-midi', 'hi': 'शुभ दोपहर', 'kn': 'ಶುಭ ಮಧ್ಯಾಹ್ನ', 'ml': 'ശുഭ മധ്യാഹ്നം', 'ta': 'மதிய வணக்கம்', 'te': 'శుభ మధ్యాహ్నం'},
        "translit": {'hi': ['shubh dopahar'], 'te': ['shubha madhyahnam']},
    },
    {
        "slug": 'welcome',
        "order": 25,
        "translations": {'en': 'Welcome', 'es': 'Bienvenido', 'fr': 'Bienvenue', 'hi': 'स्वागत है', 'kn': 'ಸ್ವಾಗತ', 'ml': 'സ്വാഗതം', 'ta': 'வருக', 'te': 'స్వాగతం'},
        "translit": {'hi': ['swagat hai'], 'te': ['swagatam']},
    },
    {
        "slug": 'congratulations',
        "order": 26,
        "translations": {'en': 'Congratulations', 'es': 'Felicidades', 'fr': 'Félicitations', 'hi': 'बधाई हो', 'kn': 'ಅಭಿನಂದನೆಗಳು', 'ml': 'അഭിനന്ദനങ്ങൾ', 'ta': 'வாழ்த்துக்கள்', 'te': 'అభినందనలు'},
        "translit": {'hi': ['badhai ho'], 'te': ['abhinandanalu']},
    },
    {
        "slug": 'happy_birthday',
        "order": 27,
        "translations": {'en': 'Happy birthday', 'es': 'Feliz cumpleaños', 'fr': 'Joyeux anniversaire', 'hi': 'जन्मदिन मुबारक हो', 'kn': 'ಹುಟ್ಟುಹಬ್ಬದ ಶುಭಾಶಯಗಳು', 'ml': 'ജന്മദിനാശംസകൾ', 'ta': 'பிறந்தநாள் வாழ்த்துக்கள்', 'te': 'పుట్టినరోజు శుభాకాంక్షలు'},
        "translit": {'hi': ['janmadin mubarak ho'], 'te': ['puttinaroju shubhakankshalu']},
    },
    {
        "slug": 'i_am_hungry',
        "order": 28,
        "translations": {'en': 'I am hungry', 'es': 'Tengo hambre', 'fr': "J'ai faim", 'hi': 'मुझे भूख लगी है', 'kn': 'ನನಗೆ ಹಸಿವಾಗಿದೆ', 'ml': 'എനിക്ക് വിശക്കുന്നു', 'ta': 'எனக்கு பசிக்குது', 'te': 'నాకు ఆకలిగా ఉంది'},
        "translit": {'hi': ['mujhe bhookh lagi hai'], 'te': ['naaku aakaliga undi']},
    },
    {
        "slug": 'i_am_thirsty',
        "order": 29,
        "translations": {'en': 'I am thirsty', 'es': 'Tengo sed', 'fr': "J'ai soif", 'hi': 'मुझे प्यास लगी है', 'kn': 'ನನಗೆ ಬಾಯಾರಿಕೆಯಾಗಿದೆ', 'ml': 'എനിക്ക് ദാഹിക്കുന്നു', 'ta': 'எனக்கு தாகமாக இருக்கிறது', 'te': 'నాకు దాహంగా ఉంది'},
        "translit": {'hi': ['mujhe pyaas lagi hai'], 'te': ['naaku dahamga undi']},
    },
    {
        "slug": 'where_is_hotel',
        "order": 30,
        "translations": {'en': 'Where is the hotel?', 'es': '¿Dónde está el hotel?', 'fr': "Où est l'hôtel ?", 'hi': 'होटल कहाँ है?', 'kn': 'ಹೋಟೆಲ್ ಎಲ್ಲಿದೆ?', 'ml': 'ഹോട്ടൽ എവിടെയാണ്?', 'ta': 'ஹோட்டல் எங்கே?', 'te': 'హోటల్ ఎక్కడ ఉంది?'},
        "translit": {'hi': ['hotel kahan hai'], 'te': ['hotel ekkada undi']},
    },
    {
        "slug": 'do_you_speak_english',
        "order": 31,
        "translations": {'en': 'Do you speak English?', 'es': '¿Hablas inglés?', 'fr': 'Parlez-vous anglais ?', 'hi': 'क्या आप अंग्रेज़ी बोलते हैं?', 'kn': 'ನಿಮಗೆ ಇಂಗ್ಲಿಷ್ ಬರುತ್ತದೆಯೇ?', 'ml': 'നിങ്ങൾക്ക് ഇംഗ്ലീഷ് അറിയാമോ?', 'ta': 'நீங்கள் ஆங்கிலம் பேசுவீர்களா?', 'te': 'మీకు ఇంగ్లీష్ వచ్చా?'},
        "translit": {'hi': ['kya aap angrezi bolte hain'], 'te': ['meeku english vachcha']},
    },
    {
        "slug": 'what_is_this',
        "order": 32,
        "translations": {'en': 'What is this?', 'es': '¿Qué es esto?', 'fr': "Qu'est-ce que c'est ?", 'hi': 'यह क्या है?', 'kn': 'ಇದೇನು?', 'ml': 'ഇത് എന്താണ്?', 'ta': 'இது என்ன?', 'te': 'ఇది ఏమిటి?'},
        "translit": {'hi': ['yah kya hai'], 'te': ['idi emiti']},
    },
    {
        "slug": 'how_to_get_to_airport',
        "order": 33,
        "translations": {'en': 'How do I get to the airport?', 'es': '¿Cómo llego al aeropuerto?', 'fr': "Comment aller à l'aéroport ?", 'hi': 'हवाई अड्डे कैसे जाऊं?', 'kn': 'ವಿಮಾನ ನಿಲ್ದಾಣಕ್ಕೆ ಹೇಗೆ ಹೋಗುವುದು?', 'ml': 'വിമാനത്താവളത്തിലേക്ക് എങ്ങനെ പോകാം?', 'ta': 'விமான நிலையத்திற்கு எப்படி செல்வது?', 'te': 'విమానాశ్రయానికి ఎలా వెళ్ళాలి?'},
        "translit": {'hi': ['hawai adde kaise jaaun'], 'te': ['vimanashrayaniki ela vellali']},
    },
    {
        "slug": 'take_care',
        "order": 34,
        "translations": {'en': 'Take care', 'es': 'Cuídate', 'fr': 'Prends soin de toi', 'hi': 'ख्याल रखना', 'kn': 'ಜೋಪಾನ', 'ml': 'സൂക്ഷിക്കണം', 'ta': 'கவனமா இரு', 'te': 'జాగ్రత్త'},
        "translit": {'hi': ['khyal rakhna'], 'te': ['jagratta']},
    },
    {
        "slug": 'see_you_tomorrow',
        "order": 35,
        "translations": {'en': 'See you tomorrow', 'es': 'Nos vemos mañana', 'fr': 'À demain', 'hi': 'कल मिलते हैं', 'kn': 'ನಾಳೆ ಸಿಗೋಣ', 'ml': 'നാളെ കാണാം', 'ta': 'நாளை பார்க்கலாம்', 'te': 'రేపు కలుద్దాం'},
        "translit": {'hi': ['kal milte hain'], 'te': ['repu kaluddam']},
    },
    {
        "slug": 'i_need_a_doctor',
        "order": 36,
        "translations": {'en': 'I need a doctor', 'es': 'Necesito un médico', 'fr': "J'ai besoin d'un médecin", 'hi': 'मुझे डॉक्टर चाहिए', 'kn': 'ನನಗೆ ವೈದ್ಯರು ಬೇಕು', 'ml': 'എനിക്ക് ഒരു ഡോക്ടറെ വേണം', 'ta': 'எனக்கு டாக்டர் தேவை', 'te': 'నాకు డాక్టర్ కావాలి'},
        "translit": {'hi': ['mujhe doctor chahiye'], 'te': ['naaku doctor kavali']},
    },
    {
        "slug": 'call_the_police',
        "order": 37,
        "translations": {'en': 'Call the police', 'es': 'Llama a la policía', 'fr': 'Appelez la police', 'hi': 'पुलिस को बुलाओ', 'kn': 'ಪೊಲೀಸರನ್ನು ಕರೆಯಿರಿ', 'ml': 'പോലീസിനെ വിളിക്കൂ', 'ta': 'போலீசை அழையுங்கள்', 'te': 'పోలీసులకు కాల్ చేయండి'},
        "translit": {'hi': ['police ko bulao'], 'te': ['policeulaku call cheyandi']},
    },
    {
        "slug": 'i_am_lost',
        "order": 38,
        "translations": {'en': 'I am lost', 'es': 'Estoy perdido', 'fr': 'Je suis perdu', 'hi': 'मैं रास्ता भूल गया हूँ', 'kn': 'ನಾನು ದಾರಿ ತಪ್ಪಿದ್ದೇನೆ', 'ml': 'എനിക്ക് വഴി തെറ്റി', 'ta': 'நான் வழி தவறிவிட்டேன்', 'te': 'నేను దారి తప్పిపోయాను'},
        "translit": {'hi': ['main raasta bhool gaya hoon'], 'te': ['nenu daari tappipoyanu']},
    },
]


def seed_phrases(apps, schema_editor):
    Phrase = apps.get_model("phrasebook", "Phrase")

    for phrase in PHRASES:
        Phrase.objects.get_or_create(
            slug=phrase["slug"],
            defaults={
                "order": phrase["order"],
                "translations": phrase["translations"],
                "translit": phrase["translit"],
            },
        )


def reverse_seed_phrases(apps, schema_editor):
    Phrase = apps.get_model("phrasebook", "Phrase")

    slugs = [phrase["slug"] for phrase in PHRASES]
    Phrase.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("phrasebook", "0002_seed_languages"),
    ]

    operations = [
        migrations.RunPython(seed_phrases, reverse_seed_phrases),
    ]
