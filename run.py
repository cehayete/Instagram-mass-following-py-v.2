from IMF import IMF
from login import password

run = IMF("_a.dvertising_", password)

run.setDonors(
    'khabib_nurmagomedov',
    'borodylia',
    'ververa',
    '_agentgirl_',
    'samburskaya ',
    'egorkreed',
    'anastasiya_kvitko',
    'm_galustyan',
    'annakhilkevich',
    'urgantcom',
    'kateclapp',
    'nagiev.universal',
    'svetabily',
    'victoriabonya',
    'missalena.92',
    'gusein.gasanov',
    'xenia_sobchak',
    'gagara1987',
    'goar_avetisyan',
    'maria__way'
)

run.start_loop(mode=1)
