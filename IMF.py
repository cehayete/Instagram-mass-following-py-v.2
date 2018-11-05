# coding=utf-8
from InstagramAPI import InstagramAPI
from PageParser import Parser
from time import sleep


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

    def setDonors(self, *donors: str):
        donors_list = []
        for donor in donors:
            p = Parser(donor)
            donors_list.append(p.getUserId())
        self.donors = donors_list

        print("Donors successfully has been setted.")
        if self.debug:
            print(self.donors)

    def start_follow(self,count: int, delay: float):
        if self.donors is not None:
            for donor in self.donors:
                c = count  # Количетсво подписчиков каждого донера на которых мы подпишемся.

                self.API.getUserFollowers(donor)
                if self.debug:
                    print(self.API.LastJson)

                for follower_data in self.API.LastJson['users']:
                    if c > 0:
                        self.API.follow(follower_data['pk'])
                        c -= 1

                        if self.API.LastJson['status'] == 'fail':
                            print("Error! Fail of follow! Please wait few minutes.")
                            self.errorPointer += 1
                            break

                        self.errorPointer = 0
                        print("You are follow {}".format(follower_data['username']))
                        sleep(delay)
        else:
            print(
                "Error! You must sets users-donors! Use IMF.setDonors(\"username1\",\"Username2\"...)"
            )

    def start_unfollow(self,count: int, delay: float):
        c = count

        self.API.getSelfUsersFollowing()
        if self.debug:
            print(self.API.LastJson)

        for user in self.API.LastJson['users']:
            if c > 0:
                self.API.unfollow(user['pk'])
                c -= 1

                if self.API.LastJson['status'] == 'fail':
                    print("Error! Fail of unfollow! Please wait few minutes.")
                    self.errorPointer += 1
                    break

                self.errorPointer = 0
                print("You are unfollow {}.".format(user['username']))
                sleep(delay)

    def start_loop(self, count: int, delay: float):
        while True:
            if self.errorPointer >= 2:
                break
            self.start_follow(count // len(self.donors), delay)
            print("Process of following do finished! Process of unfollowing are begin!")
            self.start_unfollow(count, delay)
            print("Process of unfollowing do finished! Process of following are begin!")
        print(
            "=======================\n"
            "Error! Please wait a few minutes before you try again.\n"
            "======================="
        )