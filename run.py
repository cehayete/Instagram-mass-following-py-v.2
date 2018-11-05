from IMF import IMF
from login import username, password

run = IMF(username, password)

run.setDonors(
    'buzova86',
    'timatiofficial',
    'instagramru',
    'tnt_online',
    'pavelvolyaofficial'
)

run.start_loop(
    count=1000,
    delay=30
)
