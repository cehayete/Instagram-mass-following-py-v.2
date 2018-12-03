# coding=utf-8
from InstagramAPI import InstagramAPI
from PageParser import Parser
from time import sleep


def writeLog(log: str):
    file = open('./logs.IMF','a')
    file.write(log + "<br>\n")
    file.close()

class IMF:
    def __init__(self, username: str, password: str, debug = False):
        self.API = InstagramAPI(username,password)
        self.API.login()  # Авторизация в инстаграме
        self.debug = debug

        self.donors = None
        self.errorPointer = 0

        if debug:
            print(
                "==================\n"
                "Debug mod switch on!\n"
                "=================="
            )
            writeLog(
                "==================\n"
                "Debug mod switch on!\n"
                "=================="
            )

    def setDonors(self, donors: list):
        donors_list = []
        for donor in donors:
            p = Parser(donor)
            donors_list.append(p.getUserId())
        self.donors = donors_list

        print("Donors successfully has been setted.")
        writeLog("Donors successfully has been setted.")
        if self.debug:
            print(self.donors)
            writeLog(str(self.donors))

    def start_follow(self,count: int, delay: float):
        if self.donors is not None:
            for donor in self.donors:
                c = count  # Количетсво подписчиков каждого донера на которых мы подпишемся.

                self.API.getUserFollowers(donor)
                if self.debug:
                    print(self.API.LastJson)
                    writeLog(str(self.API.LastJson))

                if donor is not None:
                    for follower_data in self.API.LastJson['users']:
                        if c > 0:
                            self.API.follow(follower_data['pk'])
                            c -= 1

                            if self.API.LastJson['status'] == 'fail':
                                print("Error! Fail of follow! Please wait few minutes.")
                                writeLog("Error! Fail of follow! Please wait few minutes.")
                                self.errorPointer += 1
                                break

                            self.errorPointer = 0
                            print("You are follow {}".format(follower_data['username']))
                            writeLog("You are follow {}".format(follower_data['username']))
                            sleep(delay)
                else:
                    self.errorPointer += 1
                    print('Error! Donor id is None.')
                    writeLog('Error! Donor id is None.')
        else:
            print(
                "Error! You must sets users-donors! Use IMF.setDonors(\"username1\",\"Username2\"...)"
            )
            writeLog(
                "Error! You must sets users-donors! Use IMF.setDonors(\"username1\",\"Username2\"...)"
            )

    def start_unfollow(self,count: int, delay: float):
        c = count

        self.API.getSelfUsersFollowing()
        if self.debug:
            print(self.API.LastJson)
            writeLog(str(self.API.LastJson))

        for user in self.API.LastJson['users']:
            if c > 0:
                self.API.unfollow(user['pk'])
                c -= 1

                if self.API.LastJson['status'] == 'fail':
                    print("Error! Fail of unfollow! Please wait few minutes.")
                    writeLog("Error! Fail of unfollow! Please wait few minutes.")
                    self.errorPointer += 1
                    break

                self.errorPointer = 0
                print("You are unfollow {}.".format(user['username']))
                writeLog("You are unfollow {}.".format(user['username']))
                sleep(delay)

    def start_loop(self, count = 500, delay = 60, mode = None):
        if mode is not None:
            if mode == 0:
                while True:
                    if self.errorPointer >= 2:
                        break
                    self.start_follow(count // len(self.donors), delay)
                    print("Process of following do finished! Process of unfollowing are begin!")
                    writeLog("Process of following do finished! Process of unfollowing are begin!")
                    self.start_unfollow(count, delay)
                    print("Process of unfollowing do finished! Process of following are begin!")
                    writeLog("Process of unfollowing do finished! Process of following are begin!")
                print(
                    "=======================\n"
                    "Error! Please wait a few minutes before you try again.\n"
                    "======================="
                )
                writeLog(
                    "=======================\n"
                    "Error! Please wait a few minutes before you try again.\n"
                    "======================="
                )
            elif mode == 1:
                num = 1
                while True:
                    print('===========\nNum of iteration: {}\n==========='.format(num))
                    writeLog('===========\nNum of iteration: {}\n==========='.format(num))

                    if self.errorPointer >= 2:
                        break
                    self.follow_to_donors(delay)

                    num += 1
            else:
                print(
                    'Unknown mode!\n'
                    '"0" - mass following.'
                    '"1" - follow and unfollow to donors.'
                )
                writeLog(
                    'Unknown mode!\n'
                    '"0" - mass following.'
                    '"1" - follow and unfollow to donors.'
                )
        else:
            print(
                "You must set mode!"
                "IMF.start_loop(mode = 0/1(or other value for help))"
            )
            writeLog(
                "You must set mode!"
                "IMF.start_loop(mode = 0/1(or other value for help))"
            )

    def follow_to_donors(self, delay: float):
        if self.donors is not None:
            if delay > 5:
                for donor in self.donors:
                    if donor is not None:
                        self.API.follow(donor)

                        if self.API.LastJson['status'] == 'fail':
                            print("Error! Fail of follow! Please wait few minutes.")
                            writeLog("Error! Fail of follow! Please wait few minutes.")
                            self.errorPointer += 1
                            break
                        else:
                            self.errorPointer = 0

                        sleep(5)
                        self.API.unfollow(donor)
                        print("OK")
                        writeLog("OK")
                        sleep(delay - 5)
            else:
                print(
                    "Error! Delay must been over 5 seconds!"
                )
                writeLog(
                    "Error! Delay must been over 5 seconds!"
                )
        else:
            print(
                "Error! You must sets users-donors! Use IMF.setDonors(\"username1\",\"Username2\"...)"
            )
            writeLog(
                "Error! You must sets users-donors! Use IMF.setDonors(\"username1\",\"Username2\"...)"
            )
