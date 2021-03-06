# -*- coding: utf-8 -*-

import locale

from bottle_utils.lazy import Lazy
from bottle_utils.common import unicode
from bottle_utils.i18n import lazy_gettext as _

COUNTRY_CHOICES = (
    ("AF", _("Afghanistan, Islamic Republic of")),
    ("AL", _("Albania, Republic of")),
    ("DZ", _("Algeria, People's Democratic Republic of")),
    ("AS", _("American Samoa")),
    ("AD", _("Andorra, Principality of")),
    ("AO", _("Angola, Republic of")),
    ("AG", _("Antigua and Barbuda")),
    ("AZ", _("Azerbaijan, Republic of")),
    ("AR", _("Argentina, Argentine Republic")),
    ("AU", _("Australia, Commonwealth of")),
    ("AT", _("Austria, Republic of")),
    ("BS", _("Bahamas, Commonwealth of the")),
    ("BH", _("Bahrain, Kingdom of")),
    ("BD", _("Bangladesh, People's Republic of")),
    ("AM", _("Armenia, Republic of")),
    ("BB", _("Barbados")),
    ("BE", _("Belgium, Kingdom of")),
    ("BM", _("Bermuda")),
    ("BT", _("Bhutan, Kingdom of")),
    ("BO", _("Bolivia, Republic of")),
    ("BA", _("Bosnia and Herzegovina")),
    ("BW", _("Botswana, Republic of")),
    ("BV", _("Bouvet Island (Bouvetoya)")),
    ("BR", _("Brazil, Federative Republic of")),
    ("BZ", _("Belize")),
    ("IO", _("British Indian Ocean Territory (Chagos Archipelago)")),
    ("SB", _("Solomon Islands")),
    ("VG", _("British Virgin Islands")),
    ("BN", _("Brunei Darussalam")),
    ("BG", _("Bulgaria, Republic of")),
    ("MM", _("Myanmar, Union of")),
    ("BI", _("Burundi, Republic of")),
    ("BY", _("Belarus, Republic of")),
    ("KH", _("Cambodia, Kingdom of")),
    ("CM", _("Cameroon, Republic of")),
    ("CA", _("Canada")),
    ("CV", _("Cape Verde, Republic of")),
    ("KY", _("Cayman Islands")),
    ("CF", _("Central African Republic")),
    ("LK", _("Sri Lanka, Democratic Socialist Republic of")),
    ("TD", _("Chad, Republic of")),
    ("CL", _("Chile, Republic of")),
    ("CN", _("China, People's Republic of")),
    ("TW", _("Taiwan")),
    ("CX", _("Christmas Island")),
    ("CC", _("Cocos (Keeling) Islands")),
    ("CO", _("Colombia, Republic of")),
    ("KM", _("Comoros, Union of the")),
    ("YT", _("Mayotte")),
    ("CG", _("Congo, Republic of the")),
    ("CD", _("Congo, Democratic Republic of the")),
    ("CK", _("Cook Islands")),
    ("CR", _("Costa Rica, Republic of")),
    ("HR", _("Croatia, Republic of")),
    ("CU", _("Cuba, Republic of")),
    ("CY", _("Cyprus, Republic of")),
    ("CZ", _("Czech Republic")),
    ("BJ", _("Benin, Republic of")),
    ("DK", _("Denmark, Kingdom of")),
    ("DM", _("Dominica, Commonwealth of")),
    ("DO", _("Dominican Republic")),
    ("EC", _("Ecuador, Republic of")),
    ("SV", _("El Salvador, Republic of")),
    ("GQ", _("Equatorial Guinea, Republic of")),
    ("ET", _("Ethiopia, Federal Democratic Republic of")),
    ("ER", _("Eritrea, State of")),
    ("EE", _("Estonia, Republic of")),
    ("FO", _("Faroe Islands")),
    ("FK", _("Falkland Islands (Malvinas)")),
    ("GS", _("South Georgia and the South Sandwich Islands")),
    ("FJ", _("Fiji, Republic of the Fiji Islands")),
    ("FI", _("Finland, Republic of")),
    ("AX", _("Åland Islands")),
    ("FR", _("France, French Republic")),
    ("GF", _("French Guiana")),
    ("PF", _("French Polynesia")),
    ("TF", _("French Southern Territories")),
    ("DJ", _("Djibouti, Republic of")),
    ("GA", _("Gabon, Gabonese Republic")),
    ("GE", _("Georgia")),
    ("GM", _("Gambia, Republic of the")),
    ("PS", _("Palestinian Territory, Occupied")),
    ("DE", _("Germany, Federal Republic of")),
    ("GH", _("Ghana, Republic of")),
    ("GI", _("Gibraltar")),
    ("KI", _("Kiribati, Republic of")),
    ("GR", _("Greece, Hellenic Republic")),
    ("GL", _("Greenland")),
    ("GD", _("Grenada")),
    ("GP", _("Guadeloupe")),
    ("GU", _("Guam")),
    ("GT", _("Guatemala, Republic of")),
    ("GN", _("Guinea, Republic of")),
    ("GY", _("Guyana, Co-operative Republic of")),
    ("HT", _("Haiti, Republic of")),
    ("HM", _("Heard Island and McDonald Islands")),
    ("VA", _("Holy See (Vatican City State)")),
    ("HN", _("Honduras, Republic of")),
    ("HK", _("Hong Kong, Special Administrative Region of China")),
    ("HU", _("Hungary, Republic of")),
    ("IS", _("Iceland, Republic of")),
    ("IN", _("India, Republic of")),
    ("ID", _("Indonesia, Republic of")),
    ("IR", _("Iran, Islamic Republic of")),
    ("IQ", _("Iraq, Republic of")),
    ("IE", _("Ireland")),
    ("IL", _("Israel, State of")),
    ("IT", _("Italy, Italian Republic")),
    ("CI", _("Cote d'Ivoire, Republic of")),
    ("JM", _("Jamaica")),
    ("JP", _("Japan")),
    ("KZ", _("Kazakhstan, Republic of")),
    ("JO", _("Jordan, Hashemite Kingdom of")),
    ("KE", _("Kenya, Republic of")),
    ("KP", _("Korea, Democratic People's Republic of")),
    ("KR", _("Korea, Republic of")),
    ("KW", _("Kuwait, State of")),
    ("KG", _("Kyrgyz Republic")),
    ("LA", _("Lao People's Democratic Republic")),
    ("LB", _("Lebanon, Lebanese Republic")),
    ("LS", _("Lesotho, Kingdom of")),
    ("LV", _("Latvia, Republic of")),
    ("LR", _("Liberia, Republic of")),
    ("LY", _("Libyan Arab Jamahiriya")),
    ("LI", _("Liechtenstein, Principality of")),
    ("LT", _("Lithuania, Republic of")),
    ("LU", _("Luxembourg, Grand Duchy of")),
    ("MO", _("Macao, Special Administrative Region of China")),
    ("MG", _("Madagascar, Republic of")),
    ("MW", _("Malawi, Republic of")),
    ("MY", _("Malaysia")),
    ("MV", _("Maldives, Republic of")),
    ("ML", _("Mali, Republic of")),
    ("MT", _("Malta, Republic of")),
    ("MQ", _("Martinique")),
    ("MR", _("Mauritania, Islamic Republic of")),
    ("MU", _("Mauritius, Republic of")),
    ("MX", _("Mexico, United Mexican States")),
    ("MC", _("Monaco, Principality of")),
    ("MN", _("Mongolia")),
    ("MD", _("Moldova, Republic of")),
    ("ME", _("Montenegro, Republic of")),
    ("MS", _("Montserrat")),
    ("MA", _("Morocco, Kingdom of")),
    ("MZ", _("Mozambique, Republic of")),
    ("OM", _("Oman, Sultanate of")),
    ("NA", _("Namibia, Republic of")),
    ("NR", _("Nauru, Republic of")),
    ("NP", _("Nepal, State of")),
    ("NL", _("Netherlands, Kingdom of the")),
    ("AN", _("Netherlands Antilles")),
    ("CW", _("Curaçao")),
    ("AW", _("Aruba")),
    ("SX", _("Sint Maarten (Netherlands)")),
    ("BQ", _("Bonaire, Sint Eustatius and Saba")),
    ("NC", _("New Caledonia")),
    ("VU", _("Vanuatu, Republic of")),
    ("NZ", _("New Zealand")),
    ("NI", _("Nicaragua, Republic of")),
    ("NE", _("Niger, Republic of")),
    ("NG", _("Nigeria, Federal Republic of")),
    ("NU", _("Niue")),
    ("NF", _("Norfolk Island")),
    ("NO", _("Norway, Kingdom of")),
    ("MP", _("Northern Mariana Islands, Commonwealth of the")),
    ("UM", _("United States Minor Outlying Islands")),
    ("FM", _("Micronesia, Federated States of")),
    ("MH", _("Marshall Islands, Republic of the")),
    ("PW", _("Palau, Republic of")),
    ("PK", _("Pakistan, Islamic Republic of")),
    ("PA", _("Panama, Republic of")),
    ("PG", _("Papua New Guinea, Independent State of")),
    ("PY", _("Paraguay, Republic of")),
    ("PE", _("Peru, Republic of")),
    ("PH", _("Philippines, Republic of the")),
    ("PN", _("Pitcairn Islands")),
    ("PL", _("Poland, Republic of")),
    ("PT", _("Portugal, Portuguese Republic")),
    ("GW", _("Guinea-Bissau, Republic of")),
    ("TL", _("Timor-Leste, Democratic Republic of")),
    ("PR", _("Puerto Rico, Commonwealth of")),
    ("QA", _("Qatar, State of")),
    ("RE", _("Reunion")),
    ("RO", _("Romania")),
    ("RU", _("Russian Federation")),
    ("RW", _("Rwanda, Republic of")),
    ("BL", _("Saint Barthelemy")),
    ("SH", _("Saint Helena")),
    ("KN", _("Saint Kitts and Nevis, Federation of")),
    ("AI", _("Anguilla")),
    ("LC", _("Saint Lucia")),
    ("MF", _("Saint Martin")),
    ("PM", _("Saint Pierre and Miquelon")),
    ("VC", _("Saint Vincent and the Grenadines")),
    ("SM", _("San Marino, Republic of")),
    ("ST", _("Sao Tome and Principe, Democratic Republic of")),
    ("SA", _("Saudi Arabia, Kingdom of")),
    ("SN", _("Senegal, Republic of")),
    ("RS", _("Serbia, Republic of")),
    ("SC", _("Seychelles, Republic of")),
    ("SL", _("Sierra Leone, Republic of")),
    ("SG", _("Singapore, Republic of")),
    ("SK", _("Slovakia (Slovak Republic)")),
    ("VN", _("Vietnam, Socialist Republic of")),
    ("SI", _("Slovenia, Republic of")),
    ("SO", _("Somalia, Somali Republic")),
    ("ZA", _("South Africa, Republic of")),
    ("ZW", _("Zimbabwe, Republic of")),
    ("ES", _("Spain, Kingdom of")),
    ("SS", _("South Sudan")),
    ("EH", _("Western Sahara")),
    ("SD", _("Sudan, Republic of")),
    ("SR", _("Suriname, Republic of")),
    ("SJ", _("Svalbard & Jan Mayen Islands")),
    ("SZ", _("Swaziland, Kingdom of")),
    ("SE", _("Sweden, Kingdom of")),
    ("CH", _("Switzerland, Swiss Confederation")),
    ("SY", _("Syrian Arab Republic")),
    ("TJ", _("Tajikistan, Republic of")),
    ("TH", _("Thailand, Kingdom of")),
    ("TG", _("Togo, Togolese Republic")),
    ("TK", _("Tokelau")),
    ("TO", _("Tonga, Kingdom of")),
    ("TT", _("Trinidad and Tobago, Republic of")),
    ("AE", _("United Arab Emirates")),
    ("TN", _("Tunisia, Tunisian Republic")),
    ("TR", _("Turkey, Republic of")),
    ("TM", _("Turkmenistan")),
    ("TC", _("Turks and Caicos Islands")),
    ("TV", _("Tuvalu")),
    ("UG", _("Uganda, Republic of")),
    ("UA", _("Ukraine")),
    ("MK", _("Macedonia, The Former Yugoslav Republic of")),
    ("EG", _("Egypt, Arab Republic of")),
    ("GB", _("United Kingdom")),
    ("GG", _("Guernsey, Bailiwick of")),
    ("JE", _("Jersey, Bailiwick of")),
    ("IM", _("Isle of Man")),
    ("TZ", _("Tanzania, United Republic of")),
    ("US", _("United States")),
    ("VI", _("United States Virgin Islands")),
    ("BF", _("Burkina Faso")),
    ("UY", _("Uruguay, Eastern Republic of")),
    ("UZ", _("Uzbekistan, Republic of")),
    ("VE", _("Venezuela, Bolivarian Republic of")),
    ("WF", _("Wallis and Futuna")),
    ("WS", _("Samoa, Independent State of")),
    ("YE", _("Yemen")),
    ("ZM", _("Zambia, Republic of")),
    ("XX", _("Disputed Territory")),
    ("XE", _("Iraq-Saudi Arabia Neutral Zone")),
    ("XD", _("United Nations Neutral Zone")),
    ("XS", _("Spratly Islands")),
)

COUNTRIES = Lazy(lambda: sorted(COUNTRY_CHOICES, key=lambda x: unicode(x[1]),
                                cmp=locale.strcoll))

COUNTRY_CODES = [""] +  [i[0] for i in COUNTRY_CHOICES]

CHANNELS = [(str(i), str(i)) for i in range(1, 14)]

HEADER = '# Auto-generated by Librarian. Do not edit manually.\n\n'

WPA_NONE = 0
WPA_COMPATIBLE = 1
WPA_SECURE = 2
WPA_MODES = (
    (WPA_NONE, _('Disabled')),
    (WPA_SECURE, _('Enabled')),
    #(WPA_COMPATIBLE, _('Low / Support older devices (WPA1/WPA2)')),
)

WIRELESS_DEFAULTS = {
    'interface': 'wlan0',
    'ssid': 'Outernet',
    'channel': '6',
    'ieee8021x': '0',
}

STANDARD = '1'
ALTERNATIVE = '2'
DRIVERS = (
    (STANDARD, _('Standard (most devices)')),
    (ALTERNATIVE, _('Alternative (Realtek-based devices)'))
)

AP_MODE = 'AP'
STA_MODE = 'STA'
MODES = (
    (AP_MODE, _('Create a hotspot')),
    (STA_MODE, _('Connect to a wireless network')),
)

NO_SECURITY = 'NONE'
WPA = 'WPA'
WEP = 'WEP'
SECURITY_PROTOCOLS = (
    (NO_SECURITY, _('No security')),
    (WPA, _('WPA')),
    (WEP, _('WEP')),
)
