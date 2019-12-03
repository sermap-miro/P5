/* AFFICHAGE DE BOITE DE DIALOGUE + MISE EN AU CENTRE de l'ecran*/
$.fn.atcenter = function () {
    this.css({
        'margin-top': -this.height() / 2 + "px",
        'margin-left': -this.width() / 2 + "px",
    })
}
$.fn.center = function () {
    this.css({
        'visibility': 'visible',
        'display': 'block',
        'position': 'fixed',
        'left': '50%',
        'top': '50%',
        'margin-top': -this.height() / 2 + "px",
        'margin-left': -this.width() / 2 + "px",
    });
    $("#updatejs *").prop('disabled', true); //
    $("#main_nav *").prop('disabled', true); //
    $("a").addClass("disabled"); // Désactivation des liens et touches externes
    $("#main_nav").addClass('disabled'); //
    $("#footer").addClass('disabled'); //
}
/* SUPPRIMER DE L'ECRAN LA  BOITE DE DIALOGUE */
$.fn.closing = function () {
    this.css({
        'visibility': 'hidden',
        'display': 'none',
    });
    $("#updatejs *").prop('disabled', false); //
    $("#main_nav *").prop('disabled', false); //
    $("a").removeClass("disabled"); // Réactivation des liens et touches externes
    $("#main_nav").removeClass('disabled'); //
    $("#footer").removeClass('disabled'); //
}
/* Suite à un réponse positive ou négative à la boite de dialogue on envoie ou pas les données au serveur */
function fermeture_pos(cible, val, number) {
    $('#alerter').closing();
    if ((number > 0) && (cible != "")) {
        $.post({
            url: cible,
            data: val,
            success: function () {
                alerter("Serveur " + cible, "Les modifications ont étés effectuées", "", "");
            }
        });
    }
}
/* Accès page conf et Calibration via un mot de passe */
function acces_conf(number) {
    var centrer;
    $('#show_mdp').center();
    centrer = setInterval("$('#show_mdp').atcenter()",500);
    var val_mdp;
    var yes = document.getElementById("y_pass").onclick = function () {
        val_mdp = document.getElementById('motdepasse').value;
        document.getElementById('motdepasse').value = "";
        $('#show_mdp').closing();
        clearInterval(centrer);
        if (val_mdp == 'Conf') {
            localStorage.setItem('mdp_conf_cali', 'tracker777');
            date_y = Date.now();
            localStorage.setItem('y', date_y);
            compteur(1800, cle = "mdp_conf_cali", value = "no");
            g_HTML(number[1]);
            if (number[0] == 'edit') {
                event_edit();
            } else if (number[0] == 'conf') {

                $.get({
                    url: '/conf.json',
                    headers: {
                        'Cache-Control': 'no-cache, no-store',
                        'Pragma': 'no-cache',
                        'Expires': '0'
                    },
                    cache: false,
                    dataType: 'json',
                    success: function (jsonObj) {
                        generate_conf(jsonObj);
                    }
                })
            }
        } else {
            alerter("Page Conf et Calib", "Mot de passe érroné", "", "");
            if (number[0] == 'edit') {
                g_HTML(number[1]);
                event_edit();
            }
        }
    };
    var no = document.getElementById("n_pass").onclick = function () {
        document.getElementById('motdepasse').value = "";
        $('#show_mdp').closing();
        clearInterval(centrer);
        if (number[0] == 'edit') {
            g_HTML(number[1]);
            event_edit();
        }
    };

}
/* Boite de dialogue : Un titre, un message , deux reponses possibles */
function alerter(type, message, cible, val) {
    var centrer;
    $('#alerter').center();
    centrer = setInterval("$('#alerter').atcenter()",500);
    $('#title_alt').text(type);
    $('#error-msg').text(message);
    var y = document.getElementById('y_alert');
    var n = document.getElementById("n_alert");
    var ent = document.getElementById("alerter");
    var no = n.onclick = function () {
        clearInterval(centrer);
        fermeture_pos(cible, val, 0);
    };
    var yes = y.onclick = function () {
        clearInterval(centrer);
        fermeture_pos(cible, val, 1);
    };
}
hostP5 = "192.168.4.1/flash"
localhost = 'localhost/P5/Wipy/FWTOOL-CLI/Version_39/Sources'
uwamp = 'localhost/Sources'
host = hostP5 // racine du projet
/* Requetes pour la page programme, manuel, et calibration */
function commande(cmd, opt) {
    $.post({
        url: cmd + opt,
        data: "PROGRAMME MANUEL CALIBRATION",
        cache: false
    });
}

function Programme_cmd(e) {
    commande("Valp=", e);
}

function Manuel_cmd(e) {
    commande("Val=", e)
}

function Calibration_cmd(e) {
    commande("Valc=", e)
}
/* Envoi de l'heure locale vers le P5 */
function maj_clock() {
    var e = new Date,
        n = e.getHours(),
        t = e.getMinutes();
    var y1 = e.getFullYear();
    var m0 = e.getMonth() + 1;
    var d1 = e.getDate();
    tosend = "H=" + n + ":" + t + ':' + y1 + ":" + m0 + ":" + d1;
    $.post({
        url: tosend,
        data: "HORLOGE",
        success: function () {
            alerter("Horloge", 'L\'horloge à été mise a jour', "", "");
            (t < 10) ? (t="0"+t):t;
            (n < 10) ? (n="0"+n):t;
            document.getElementById('m_time').innerHTML = 'P5 : ' + n + ':' + t;
        }
    })
}

/* Element auquel toute nos pages sont affichées */
function g_HTML(texte) {
    document.getElementById('updatejs').innerHTML = texte;
}
/* Fonction remontant la barre de navigation en cliquant sur le contenu principal */
function main_view() {
    var elm = document.getElementById('navbarColor01');
    if (elm.className === 'navbar-collapse collapse show') {
        $('#navbarColor01').collapse('hide');
    }
}
x = 0;
/* A l'ouverture de la page */
function init() {
    // Affichage de l'heure locale dans la div comportant l'id 'now' 
    g_time(); // Affichage de l'heure du P5 
    if (localStorage.getItem("y") === null) {
        localStorage.setItem("y", 0); // Initialisation des variables locales
    }
    if (localStorage.getItem("mdp_conf_cali") === null) {
        localStorage.setItem("mdp_conf_cali", "no");
    }
    compteur(1800, cle = "mdp_conf_cali", value = "no"); // Compteur de 30 pour l'activation de la page CONF et CALI
    set_active();
}

function compteur(nb, cle, value) {
    var diff = Date.now();
    if ((diff - localStorage.getItem('y')) >= nb * 1000) {
        localStorage.setItem(this.cle, this.value);
    } else {
        setTimeout("compteur(" + nb + ",this.cle,this.value)", "1000");
    }
}
/* Appel de la fonction venant du menu */
/* Affichage du contenu des menus */
function comd(number) {
    $("body").css("background-image", "none"); // Suppression l'image en arriere plan SERMAP
    if (number[0] == 'home') {
        $("body").css("background-image", ""); // Affichage à nouveau du Background
    }
    if ((number[0] == 'calibration') || (number[0] == 'conf') || (number[0] == 'edit')) {

        cali = localStorage.getItem('mdp_conf_cali');
        if (cali != 'tracker777') {
            acces_conf(number);
        } else {
            g_HTML(number[1]);
            // Affichage du contenu
            if (number[0] == 'conf') {

                $.get({
                    url: 'assets/json/conf.json',
                    headers: {
                        'Cache-Control': 'no-cache, no-store',
                        'Pragma': 'no-cache',
                        'Expires': '0'
                    },
                    cache: false,
                    dataType: 'json',
                    success: function (jsonObj) {
                        generate_conf(jsonObj);
                    }
                })
            }
        }
    } else {
        g_HTML(number[1]); // Affichage du contenu 
    }
    if (number[0] == 'info') {
        Info(); // Affichage des information du ¨P5 
        if (x) {
            clearInterval(x);
        }
        x = setInterval(Info, 5000); // Actualisation toutes les 5 secondes
    } else {
        clearInterval(x); // Arrêt actualisation
    }
}

function set_active() {
    var logo = document.getElementById("home");
    logo.addEventListener("click", function () {
        var acti = document.getElementsByClassName("bright-miro");
        if (acti.length > 0) {
            acti[0].className = acti[0].className.replace("bright-miro", "nav-link");
        }
    })
    var li_btn = document.getElementById("navbarColor01");
    var btns = li_btn.getElementsByTagName("a");
    for (var i = 0; i < btns.length - 2; i++) {
        btns[i].addEventListener("click", function () {
            var current = document.getElementsByClassName("bright-miro");
            // If there's no active class
            if (current.length > 0) {
                current[0].className = current[0].className.replace("bright-miro", "nav-link");
            }
            // Add the active class to the current/clicked button
            this.className = "bright-miro";
        });
    }
}

function g_wifi() {
    comd(wifi);
    $.get({
        url: 'assets/json/channel.json',
        headers: {
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        },
        cache: false,
        dateType: 'json',
        success: function (jsonObj) {
            var channel = parseInt(jsonObj["canal"]);
            var txt = '';
            for (var i = 1; i < 12; i++) {
                txt += '<OPTION value="' + i + '" ';
                if (i == channel) {
                    txt += 'selected';
                }
                txt += ' >' + i + '</OPTION>';
            }
            document.getElementById('c1').innerHTML = txt;

        },
        error: function () {
            var txt = '';
            for (var i = 1; i < 12; i++) {
                txt += '<OPTION value="' + i + '" >' + i + '</OPTION>';
            }
            document.getElementById('c1').innerHTML = txt;

        }
    });
}
/* Fonction de recuperation de l'heure du P5 */
function g_time() {
    /* Demande ajax de type GET */
    $.get({
        url: 'assets/json/clock.json',
        headers: {
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        },
        cache: false,
        dataType: 'json', 
        error: function() {
              not_ok();
            },
        // lors de la recuperation du fichier on fait appel à up_date time pour traiter le fichier JSON
        success: function (jsonObj) {
            up_date_time(jsonObj);
        }
       
    });
    setTimeout('g_time();', 15000); // Actualisation toutes les 15 secondes
}
function not_ok(){
    document.getElementById("etat_co").innerHTML = "Non connecté";
}
/* Recuperation et affichage de l'heure */
function up_date_time(jsonObj) {
    document.getElementById("etat_co").innerHTML = "Connecté";
    var l_heure = jsonObj['h'];
    var la_minute = jsonObj['m'];
    (l_heure < 10) ? (l_heure = "0" + l_heure) : l_heure;
    (la_minute < 10) ? (la_minute = "0" + la_minute) : la_minute;
    document.getElementById('m_time').innerHTML = 'P5 : ' + l_heure + ':' + la_minute;
}
/* Le tableau est généré, on fait appel au serveur  pour récupurer les informations */
function Info() {
    try {
        if (document.getElementById('derniere_alarme')) { // On verifie que la page info est affichée
            $.get({
                url: 'assets/json/info.json',
                headers: {
                    'Cache-Control': 'no-cache, no-store',
                    'Pragma': 'no-cache',
                    'Expires': '0'
                },
                cache: false,
                dataType: 'json',
                success: function (jsonObj) {
                    generate_info(jsonObj);
                }
            })
        } else {
            clearInterval(x);
        }
    } catch (error) {
        console.log(error);
    }
}
/* Fichier JSON récupéré, affichage des informations */
function generate_info(jsonObj) {
    try {
        var T_vol = jsonObj["Temps de vol"];
    } catch (error) {
        console.log(error);
    }
    try {
        var mdp = jsonObj["mdp wifi"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('derniere_alarme').innerHTML = jsonObj["Derniere alarme"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('etat_p5').innerHTML = jsonObj["Etat P5"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('etat_p_p5').innerHTML = jsonObj["Etat precedant"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('pions').innerHTML = jsonObj["Pions"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('tension').innerHTML = jsonObj["Tension"] + ' V';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('c_pion').innerHTML = jsonObj["Capteur pion"] ? '<span class="badge badge-dark">Metal Absent</span>' : '<span class="badge badge-primary">Metal Présent</span>';
    } catch (error) {
        console.log(error);
    }
    try {


        document.getElementById('c_capot').innerHTML = jsonObj["Capteur capot"] ? '<span class="badge badge-success">En place</span>' : '<span class="badge badge-danger">En défaut</span>';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('arret_urgence').innerHTML = jsonObj["Arret urgence"] ? '<span class="badge badge-danger">En Urgence</span>' : '<span class="badge badge-success">Position Normal</span>';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('relais').innerHTML = jsonObj["Relais"] ? 'Activé' : 'Désactivé';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('im1').innerHTML = jsonObj["i Moteur 1"] + ' A';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('im2').innerHTML = jsonObj["i Moteur 2"] + ' A';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('patinage').innerHTML = jsonObj["Patinage"] + ' s';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('t_pion').innerHTML = jsonObj["Temps pion"] + '  ms';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('t_platine').innerHTML = jsonObj["Temps platine"] + ' ms';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('t_pelle').innerHTML = jsonObj["Temps pelle"] + ' s';
    } catch (error) {
        console.log(error);
    }
    if (T_vol <= 60) {
        document.getElementById('t_vol').innerHTML = Math.round10(T_vol) + ' s';
    } else if (T_vol < 3600) {
        document.getElementById('t_vol').innerHTML = Math.round10(T_vol / 60, -2) + ' min';
    } else {
        document.getElementById('t_vol').innerHTML = Math.round10(T_vol / 3600, -2) + ' h';
    }
    try {
        document.getElementById('v_pic_wipy').innerHTML = jsonObj["Version PIC"] + ':' + jsonObj["Version Wipy"];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('t_demarrage').innerHTML = Math.round10(jsonObj["Temps demarrage"], -2) + ' s';
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('w_name').innerHTML = jsonObj["WIFI"];
    } catch (error) {
        console.log(error);
    }
    try {

        document.getElementById('w_pass').innerHTML = (mdp != "undefined") ? mdp : '';
    } catch (error) {
        console.log(error);
    }
}
// Afichage de la page Configuration
// function f_conf(){
// comd(conf);
// $.get({
// url : '/conf.json',
// headers: {
// 'Cache-Control': 'no-cache, no-store',
// 'Pragma': 'no-cache', 
// 'Expires': '0'
// },
// cache : false,
// dataType : 'json' ,
// success : function (jsonObj){
// generate_conf(jsonObj);}
// })	
// }
// Affichage du contenu de la page configuration
function generate_conf(jsonObj) {
    try {
        document.getElementById('Consigne_Moteur').value = jsonObj['Consigne Moteur'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Consigne_Pelle').value = jsonObj['Consigne Pelle'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Seuil_Pelle').value = jsonObj['Seuil Pelle'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Consigne_Bequille').value = jsonObj['Consigne Bequille'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Seuil_Bequille').value = jsonObj['Seuil Bequille'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Patinage').value = jsonObj['Patinage'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Temps_Pion').value = jsonObj['Temps Pion'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Temps_Platine').value = jsonObj['Temps Platine'];
    } catch (error) {
        console.log(error);
    }
    try {
        document.getElementById('Temps_Pelle').value = jsonObj['Temps Pelle'];
    } catch (error) {
        console.log(error);
    }
}
/* Affichage de la page edit */
function g_edit() {
    comd(edit);
    event_edit();
}
/* Génération de la page édit*/
function event_edit() {
    var access = localStorage.getItem('mdp_conf_cali'); 
    var x = document.getElementById('opt_edit'); 
    var tab = ['Standard', 'Pailleux', 'DVT', 'MultiTas'];

    if (access == 'tracker777') { /* Si le mot de passe est bon alors on affiche les fichiers Standard, Pailleux, DVT, Multitas */
        for (var add in tab) {
            var opt = document.createElement('option');
            opt.value = tab[add];
            opt.innerHTML = tab[add];
            x.appendChild(opt);
        }
    }

    x.addEventListener("change", function () { // Affichage des fichiers 1 à 9 et Retour + Standard,Multitas,Pailleux,DVT,MultiTas
        if (x.value != '') {
            $.get({
                url: 'prgm/' + x.value + '.txt', //Recuperation du texte
                headers: {
                    'Cache-Control': 'no-cache, no-store, must-revalidate',
                    'Pragma': 'no-cache',
                    'Expires': '0'
                },
                cache: false,
                dataType: 'text',
                success: function (contenu) {
                    document.getElementById('put_text').innerHTML = contenu; // Affichage de la récupération
                }
            });
        } else {
            document.getElementById('put_text').innerHTML = "";
        }
    });
}
// Page Planning 
function g_planning() {
    comd(planning); // Affichage en-tête planning 
    $.get({
        url: 'planning.txt',
        headers: {
            'Cache-Control': 'no-cache, no-store',
            'Pragma': 'no-cache',
            'Expires': '0'
        },
        cache: false, 
        dataType: 'text',
        success: function (contenu) {
            var texte = ''; 
            var reg = new RegExp(["\n"]); 
            var reg2 = new RegExp([":"]);
            var col = 1;
            var tab_opt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Standard', 'Pailleux', 'DVT', 'MultiTas'];
            tab_l = contenu.split(reg); // On coupe le texte en saut de ligne
            for (var ligne in tab_l) {
                tab_c = tab_l[ligne].split(reg2); // On coupe la ligne en 4 grace à :
                if (tab_c.length == 4) {
                    var txt_opt = '';
                    if (tab_c[0] == 'True') {
                        var act = 'checked';
                    } else {
                        var act = '';
                    }
                    var h = parseInt(tab_c[1]);
                    var m = parseInt(tab_c[2]);
                    var prgm = tab_c[3];
                    texte += '<tr><th scope="col">' + col + '</th><th scope="col"><input class="case_1" type="text" name="h' + col + '" id="h' + col + '"value="' + h + '" min="0" max="23" size="2"/></th><th scope="col"><input class="case_1" type="text" name="m' + col + '" id="m' + col + '"value="' + m + '" min="0" max="59" size="2"></th><th scope="col"><input type="checkbox" id="v' + col + '" name="c' + col + '" ' + act + '/></th><th scope="col"><SELECT name="p{0}" size="1" id="opt_' + col + '">';
                    for (var s_opt in tab_opt) {
                        txt_opt += '<OPTION value="' + tab_opt[s_opt] + '" ';
                        if (tab_c[3] == tab_opt[s_opt]) {
                            txt_opt += 'selected';
                        }
                        txt_opt += ' >' + tab_opt[s_opt] + '</OPTION>';
                    }
                    texte += txt_opt + '</SELECT></th></tr>'
                    col += 1;
                }
            }
            document.getElementById('f_tab').innerHTML = texte;
        }
    });
}
// En appuyant sur le bouton sauvegarder de la planning on tombe sur cette fonction
function save_plan() {
    var x = 0;
    var y = 1;
    var a_z = 0;
    var reg = new RegExp(["^[0-9]{1,2}$"]);
    var tab_id = new Array(20);
    var tab_h = new Array(20);
    var tab_m = new Array(20);
    var tab_c = new Array(20);
    var tab_p = new Array(20);
    var nom_fnc = "Planning";
    var valeurs = '',
        e_h = 0,
        e_m = 0;
    for (x = 0; x < 20; x++) {
        y = x + 1
        tab_id[x] = y;
        var v1;
        var v2;
        tab_h[x] = document.getElementById('h' + y).value;
        tab_m[x] = document.getElementById('m' + y).value;
        m_h = "Les entrées des Heures sont érronées"
        m_m = "Les entrées des Minutes sont érronées"
        if ($('input[name=c' + y + ']').is(':checked')) {
            tab_c[x] = true;
            valeurs += 'c' + y + '=True& ';
        } else {
            tab_c[x] = false;
            valeurs += 'c' + y + '=False& ';
        }
        tab_p[x] = document.getElementById('opt_' + y).value;
        valeurs += 'h' + y + '=' + tab_h[x] + '& ' + 'm' + y + '=' + tab_m[x] + '& ' + 'p' + y + '=' + tab_p[x] + '& \n';
        tab_h[x] > 23 ? e_h = +1 : e_h = e_h;
        tab_m[x] > 59 ? e_m = +1 : e_m = e_m;
        v1 = reg.test(tab_h[x]);
        v2 = reg.test(tab_m[x]);
        if (!v1 || !v2) {
            a_z += 1;
        }

    }
    console.log(valeurs);
    if (e_h == 0 && e_m == 0 && !a_z) {
        alerter(nom_fnc, "Êtes vous sur de modifier le planning ?", '/T3', valeurs);
    } else if (a_z) {
        alerter(nom_fnc, "Veuillez mettre que des chiffres dans les entrées H et M", "", "");
    } else if (e_h) {
        e_m > 0 ? alerter(nom_fnc, m_h + '\n' + m_m, "", "") : alerter(nom_fnc, m_h, "", "");
    } else {
        alerter(nom_fnc, m_m, "", "");
    }
}
// Lorsque on appuye sur le bouton de changement de WIFI
function change_wifi() {
    var reg = new RegExp('^[a-zA-Z0-9_-]{8,20}');
    var reg2 = new RegExp('^[a-zA-Z0-9]{0,8}');
    var wifi_name = document.getElementById('n1').value;
    var pass_ = document.getElementById('p1').value;
    var canal = document.getElementById('c1').value;

    data = 'n1=' + wifi_name + '& p1=' + pass_ + '& c1=' + canal + '&';
    if (!wifi_name.match(reg2)) {
        alerter("Wifi", "Veuillez mettre un nom de wifi correct(Maximum 8 caractères, avec des lettres, ou laissez la case vide)", '', '');
    } else {
        if (pass_.match(reg) || pass_ == '') {

            $.post({
                url: '/Wifi',
                data: data,
                success: function () {
                    alerter("Serveur " + cible, "Les modifications ont étés effectuées", "", "");
                    if (wifi_name != '') {

                        document.getElementById('w_name').innerHTML = 'Nom Wifi : P5 -' + wifi_name;
                    } else {
                        document.getElementById('w_name').innerHTML = 'Nom Wifi : P5';
                    }
                    document.getElementById('w_pass').innerHTML = 'Mot de passe : ' + pass_;
                    document.getElementById('w_channel').innerHTML = 'Canal: ' + canal;
                }
            });

        } else {
            alerter('Wifi', 'Veuillez mettre un mot de passe correct(Minimum 8 caractères à 20, sans espaces ni caractères speciaux.)  ', '', '');
        }
    }
}
// En appuyant sur le bouton sauvegarder de la page configuration on tombe sur cette fonction
function save_conf() {
    var tab = [document.getElementById('Consigne_Moteur').name, document.getElementById("Consigne_Pelle").name, document.getElementById("Seuil_Pelle").name, document.getElementById("Consigne_Bequille").name, document.getElementById("Seuil_Bequille").name, document.getElementById("Patinage").name, document.getElementById("Temps_Pion").name, document.getElementById("Temps_Platine").name, document.getElementById("Temps_Pelle").name]
    var tab2 = [document.getElementById('Consigne_Moteur').value, document.getElementById("Consigne_Pelle").value, document.getElementById("Seuil_Pelle").value, document.getElementById("Consigne_Bequille").value, document.getElementById("Seuil_Bequille").value, document.getElementById("Patinage").value, document.getElementById("Temps_Pion").value, document.getElementById("Temps_Platine").value, document.getElementById("Temps_Pelle").value];
    var texte = '';
    var reg = new RegExp(["^[0-9]+$"]);
    var z_c = 'Configuration';
    var vide = 0,
        cons = 0,
        pat = 0,
        t_ms = 0,
        diff = 0,
        neg = 0,
        a_z = 0;
    if ((tab2[5] >= 255) || (tab2[8] >= 255)) {
        pat = 1;
    }
    for (nb in tab) {
        if (!reg.test(tab2[nb])) {
            a_z += 1;
        }
        if (tab2[nb] == '') {
            vide += 1;
        }
        if (tab2[nb] <= 0) {
            neg += 1;
        }

        texte += tab[nb] + '=' + tab2[nb] + '& \n';
        if (nb <= 4) {
            if (tab2[nb] > 20) {
                cons += 1;
            }
        }
        if (5 < nb < 8) {
            if (tab2[nb] >= 25500) {
                t_ms += 1;
            }
        }

    }
    try {
        diff = tab2[7] - tab2[6];
    } catch (error) {
        console.log(error);
    }

    if (vide == 1) {
        alerter(z_c, "Il y a 1 case vide, remplissez la!", "", "");
    } else if (a_z) {
        alerter(z_c, "Veuillez mettre que des chiffres , svp!", "", "");
        console.log(a_z);
    } else if (vide) {
        alerter(z_c, "Il y a " + vide + " cases vides, remplissez les!", "", "");
    } else if (cons) {
        alerter(z_c, "Il y a " 
        + cons + " consigne(s) au dessus de 20 A, corrigez la/les!", "", "");
    } else if (pat) {
        alerter(z_c, "Les variables de patinage et de Temps pelle doivent être inferieure à 255 secondes!", "", "");
    } else if (t_ms) {
        alerter(z_c, "Les valeurs de temps pions et platine doivent être inferieures à 25500!", "", "");
    } else if (diff < 2800) {
        alerter(z_c, "L'écart entre le temps platine et temps pion doit etre supérieur ou égal à 2800 ms\nActuellement la difference est de " + diff + " ms.", "", "");
    } else if (neg) {
        alerter(z_c, "Aucune valeure nulle ou négative n'est autorisée", "", "");
    } else {
        (alerter(z_c, 'Êtes vous sur de vouloir assigner ces valeurs ?\n', 'Conf', texte));
    }
}
// En appuyant sur le bouton sauvegarder de la page edition on tombe sur cette fonction
function save_edit() {
    var valeur = document.getElementById('opt_edit').value
    if (valeur != '') {
        var ed = "Edition " + valeur + ".txt"
        var val_txt = document.getElementById('put_text').value
        var fichier = 'p1=' + valeur + '&\n';
        var contenu = 'd1=' + val_txt + '&\n';
        var mode = 's1=W&';
        var erl = '',
            err = 0,
            ligne = 0,
            ev = 0;
        var tosend = fichier + contenu + mode;
        var reg = new RegExp("(^[ADMPRSE] [1-9][0-9]{0,3}$)|(^O [DG]$)|(^[ARBL]$)|(^[AR] 0$)|(^\#[\t A-Za-z0-9_'*\#\-]*$)|(^[\t ]*$)", "gm");
        var reg2 = new RegExp("[\n]");
        console.log(val_txt.match(reg));
        tab = val_txt.match(reg);
        tab2 = val_txt.split(reg2);
        if (val_txt.length > 0) {
            if (tab.length != tab2.length) {
                err = 1;
            }
            for (ev in tab2) {
                if (tab[ev] != tab2[ev]) {
                    erl = tab2[ev];
                    ligne = ev;
                    ligne++;
                    break;
                }
            }
            if (!err) {
                alerter(ed, 'Êtes vous sur de vouloir modifier le fichier ' + valeur + '.txt?\n', "/Edit", tosend);
            } else {
                alerter(ed, "Ligne " + ligne + " : " + erl + " n'est pas reconnu", "", "");
            }
        } else if (tab2.length == null) {
            alerter('Edition', 'Votre contenu est vide', "", "");
        } else {
            alerter('Edition', ' Ligne 0 : ' + val_txt + ' n\'est pas reconnu', "", "");
        }
    } else {
        alerter('Edition', 'Veuillez selectionner le fichier à éditer', "", "");
        return false;
    }
}

// En appuyant sur le bouton sauvegarder de la page Heure on tombe sur cette fonction
function save_h() {
    var h1 = $("#h1").val();
    var m1 = $("#m1").val();
    var e = new Date;
    var reg = new RegExp(["^[0-9]{1,2}$"]);
    var y1 = e.getFullYear();
    var m0 = e.getMonth() + 1;
    var d1 = e.getDate();
    if (h1 != '' && m1 != '' && reg.test(h1) && reg.test(m1)) {
        if (h1 <= 23 && h1 >= 0 && m1 <= 59 && m1 >= 0) {

            var dataString = 'h1=' + h1 + '& m1=' + m1 + '& y1=' + y1 + '& m0=' + m0 + '& d1=' + d1 + '&';
            var phrase = "Mise à jour Horloge " + dataString;
            console.log(phrase);
            $.post({
                url: "/Clock",
                data: dataString,
                success: function () {
                    alerter("Horloge", "L'horloge à été mis à jour", "", "");
                    (h1 < 10) ? (h1="0"+h1):h1;
                    (m1 < 10) ? (m1="0"+m1):m1;
                    document.getElementById('m_time').innerHTML = 'P5 : ' + h1 + ':' + m1;
                }
            });

            return false;
        } else {
            alerter("Horloge", "Les entrées ne sont pas attribuables", "", "");
        }
    } else if (!reg.test(h1) || !reg.test(m1)) {
        alerter("Horloge", "Seuls les chiffres sont acceptés", "", "");
    } else {
        alerter("Horloge", "Veuillez remplir les entrées s'il vous plait", "", "");
    }
}

(function () {

    function decimalAdjust(type, value, exp) {
        // Si l'exposant vaut undefined ou zero...
        if (typeof exp === 'undefined' || +exp === 0) {
            return Math[type](value);
        }
        value = +value;
        exp = +exp;
        // Si value n'est pas un nombre 
        // ou si l'exposant n'est pas entier
        if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0)) {
            return NaN;
        }
        // Décalage
        value = value.toString().split('e');
        value = Math[type](+(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp)));
        // Re "calage"
        value = value.toString().split('e');
        return +(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp));
    }

    // Arrondi décimal
    if (!Math.round10) {
        Math.round10 = function (value, exp) {
            return decimalAdjust('round', value, exp);
        };
    }
    // Arrondi décimal inférieur
    if (!Math.floor10) {
        Math.floor10 = function (value, exp) {
            return decimalAdjust('floor', value, exp);
        };
    }
    // Arrondi décimal supérieur
    if (!Math.ceil10) {
        Math.ceil10 = function (value, exp) {
            return decimalAdjust('ceil', value, exp);
        };
    }

})();
var home = ["home", '', "home"];
var clock = ["clock", '<div class="container center-block"><div class="row center-block" style=""><div class="center-block" style="float:none;margin: auto;"><div class="row prgm-nav"><li style="margin: auto;"><a onclick="save_h()" class="btn btn-miro mb-3" id="clk_save">Sauvegarder</a></li></div><div class="row"><p style="margin: auto;">Heure:</p><p style="margin: auto;">Minute:</p></div><div class="row center-block" style="margin: auto;"><input style="margin: auto;" type="text" id="h1" name="h1"  pattern="[0-9]{1,2}" size="5" ><input type="text" name="m1" id="m1" size="5" pattern="[0-9]{1,2}" style="margin: auto;"></div></div></div></div>', "page_clk"];
var wifi = ["wifi", '<div class="container"><div class="row"><div class="col-12 "><div class="form-group"><div>Nouveau nom Wifi = "P5 - {Nom saisi}"</div><input type="text" id="n1" name="n1" maxlength="8" pattern="[a-zA-Z0-9_ ]{1,8}"></div><div class="form-group"><div>Mot de passe</div> <input type="text" id="p1" name="p1" minlength="8" maxlength="20" pattern="[a-zA-Z0-9_-]{8,20}"><div>Caractères autorisés : chiffre et lettre (minuscule et majuscule) ayant minumum 8 Caractères</div></div><div class="form-group"><label>Canal</label> <SELECT name="c1" id="c1" size="1" class="custom-select"></SELECT></div><button onclick="change_wifi()" class="btn btn-miro">Sauvegarde</button></div></div><div class="row"><div class="col-12 wifi-change"><div class="col-4" id="w_name"></div><div class="col-4" id="w_pass"></div><div class="col-4" id="w_channel"></div></div></div></div>', "page_wifi"];
var planning = ["planning", '<div class="container"><div class="row"><div class="col-12"><button onclick="save_plan()" class="btn btn-miro mb-3">Sauvegarder</button><div class="table-responsive"><table class="table"><thead><tr><th scope="col">#</th><th scope="col">Heure</th><th scope="col">Minute</th><th scope="col">A / D</th><th scope="col">Programme</th></tr></thead><tbody id="f_tab"></tbody></table></div></div></div>', "page_plan"];
var edit = ["edit", '<div class="container"><div class="row"><div class="col-12"><button onclick="save_edit()" class="btn btn-miro mb-3" >Sauvegarder</button><p><SELECT name="p1" size="1" class="custom-select"id="opt_edit"><OPTION value="" selected>Choisissez le fichier à éditer</OPTION><OPTION value="1">1</OPTION><OPTION value="2">2</OPTION><OPTION value="3">3</OPTION><OPTION value="4">4</OPTION><OPTION value="5">5</OPTION><OPTION value="6">6</OPTION><OPTION value="7">7</OPTION><OPTION value="8">8</OPTION><OPTION value="9">9</OPTION><OPTION value="Retour">Retour</OPTION> </SELECT></p><TEXTAREA class="form-control" name="d1" rows=15 cols=15 id="put_text"></TEXTAREA></div></div></div>', "page_edit"];
var info = ["info", '<div class="container"><div class="row"><div class="col-12"><div class="table-responsive"><table class="table"><tr><td>Dernière alarme</td><td id="derniere_alarme" class="text-right"></td><tr><td>Etat P5</td><td id="etat_p5" class="text-right"></td><tr><td>Etat précédant P5</td><td id="etat_p_p5"class="text-right"></td><tr><td>Pions</td><td id="pions"class="text-right"></td><tr><td>Batterie</td><td id="tension"class="text-right"></td><tr><td>Capteur pion</td><td id="c_pion"class="text-right"></td><tr><td>Capteur capot</td><td id="c_capot" class="text-right"></td><tr><td>Arret Urgence</td><td id="arret_urgence" class="text-right"></td><tr><td>Relais</td><td id="relais"class="text-right"></td><tr><td>I Moteur 1</td><td id="im1"class="text-right"></td><tr><td>I Moteur 2</td><td id="im2"class="text-right"></td><tr><td>Patinage</td><td id="patinage"class="text-right"></td><tr><td>Temps pion</td><td id="t_pion"class="text-right"></td><tr><td>Temps platine</td><td id="t_platine"class="text-right"></td><tr><td>Temps pelle</td><td id="t_pelle"class="text-right"></td><tr><td>Temps de vol</td><td id="t_vol"class="text-right"></td><tr><td>Version PIC:Wipy</td><td id="v_pic_wipy"class="text-right"></td><tr><td>Temps de démarrage</td><td id="t_demarrage"class="text-right"></td><tr><td>Nom wifi <a onclick=g_wifi()>SSID</a></td><td id="w_name"class="text-right"></td><tr><td>Mot de passe wifi</td><td id="w_pass"class="text-right"></td></table></div></div></div></div>', "page_info"];
var manu = ["manu", '<div class="container"><div class="row"><div class="col-12"><ul class="miro-nav"><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(1)">Cycle (Standard)</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(2)">Avant</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(3)">Lever Pelle</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(4)">Sort (Bequille)</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(5)">STOP</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(6)">Rentre (Bequille)</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(7)">Cycle (Retour)</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(8)">Arrière</a></li><li><a class="btn btn-miro prgm_manu" onclick="Manuel_cmd(9)">Baisser Pelle</a></li></ul></div></div></div>', "page_manu"];
var calibration = ["calibration", '<div class="container"><div class="row"><div class="col-12"><div class="pad19"><div class="row mb-2"><div class="col-12"><ul class="prgm-nav"><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(1)">10 V</a></li><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(2)">30 V</a></li><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(3)">Bip</a></li></ul></div></div></div><div class="row mb-2"><div class="col-12"><ul class="prgm-nav"><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(4)">LED ON</a></li><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(5)">LED OFF</a></li><li><a class="btn btn-miro btn-lg" onclick="Calibration_cmd(6)">00:00</a></li></ul></div></div></div></div></div></div>', "page_cali"];
var programme = ["programme", '<div class="container"><div class="row"><div class="col-12"><div class="pad19"><div class="row"><div class="col-12"><ul class="prgm-nav"><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(1)">1</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(2)">2</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(3)">3</a></li> </ul></div></div><div class="row"><div class="col-12"><ul class="prgm-nav"><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(4)">4</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(5)">5</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(6)">6</a></li></ul></div></div><div class="row"><div class="col-12"><ul class="prgm-nav"><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(7)">7</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(8)">8</a></li><li><a class="btn btn-miro btn-lg" onclick="Programme_cmd(9)">9</a></li></ul></div></div></div><ul class="miro-nav"><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(10)">Standard</a></li><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(11)">Pailleux</a></li><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(12)">DVT</a></li><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(13)">MultiTas</a></li><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(14)">Retour</a></li><li><a class="btn btn-miro prgm_manu" onclick="Programme_cmd(15)">STOP</a></li></ul></div></div></div>', "page_prog"];
var conf = ["conf", '<div class="container"><div class="row"><div class="col-12 "><button class="btn btn-miro" onclick="save_conf()">Enregistrer les modifications</button><div class="col-6 conf"><div class="row"><div class="col-6 name_conf"><label>Consigne Moteur:</label></div><div class="col-4 in_conf"><input required="required" type="text" id="Consigne_Moteur" name="m1"  min="0" max="50" size="5"/></div><div class="col-2 u_conf"> A</div></div><div class="row"><div class="col-6 name_conf"><label>Consigne Pelle: </label></div><div class="col-4 in_conf"><input required="required" id="Consigne_Pelle" type="text" name="c1"  min="0" max="50"size="5"/></div><div class="col-2 u_conf"> A</div></div><div class="row"><div class="col-6 name_conf"><label>Seuil Pelle: </label></div><div class="col-4 in_conf"><input required="required" id="Seuil_Pelle" type="text" name="s1"  min="0" max="50" size="5"/></div><div class="col-2 u_conf"> A</div></div><div class="row"><div class="col-6 name_conf"><label>Consigne Bequille: </label></div><div class="col-4 in_conf"><input type="text" required="required" id="Consigne_Bequille" name="b1"  min="0" max="50" size="5"/></div><div class="col-2 u_conf"> A</div></div><div class="row"><div class="col-6 name_conf"><label>Seuil Bequille: </label></div><div class="col-4 in_conf"><input required="required" id="Seuil_Bequille" type="text" name="d1"  min="0" max="50" size="5"/></div><div class="col-2 u_conf"> A</div></div><div class="row"><div class="col-6 name_conf"><label>Patinage: </label></div><div class="col-4 in_conf"><input id="Patinage" type="text" required="required" name="p1"  min="0" max="500" size="5"/></div><div class="col-2 u_conf"> s</div></div><div class="row"><div class="col-6 name_conf"><label>Temps Pion: </label></div><div class="col-4 in_conf"><input type="text" id="Temps_Pion" required="required" name="i1"  min="0" max="3000" size="5"/></div><div class="col-2 u_conf"> ms</div></div><div class="row"><div class="col-6 name_conf"><label>Temps Platine: </label></div><div class="col-4 in_conf"><input required="required" id="Temps_Platine" type="text" name="l1"  min="0" max="5000" size="5"/></div><div class="col-2 u_conf"> ms</div></div><div class="row"><div class="col-6 name_conf"><label>Temps pelle: </label></div><div class="col-4 in_conf"><input id="Temps_Pelle" required="required" type="text" name="e1"  min="0" max="600" size="5"/></div><div class="col-2 u_conf"> s</div></div></div></div></div></div>', "page_conf"];
/* Demarrage des fonctions a l'ouverture de la page HTML */
$(document).ready(function () {
    init();
});