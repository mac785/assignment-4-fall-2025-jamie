# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: Jamie Moseley
## EID : jbm4577
## Section: ME396P

"""

import random

nslots = 16 # 30 minute slots in an 8 hour day
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
classLength = {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}
nDays = len(week)
startOfDay = 9


class personSchedule:   

    
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.classes = kwargs['classes']

        self.schedule = {}

        for i in self.classes:
            tempDay = [0]*nslots
            numClasses = self.classes[i]
            classTimes = self.generateTimes(numClasses, classLength[i])
            for j in classTimes:
                for k in range(classLength[i]):
                    tempDay[j + k] = 1
            self.schedule[i] = tempDay
            
        
    def add_event(self, time_dict_input):
        day = time_dict_input['day']
        from_text = time_dict_input['time']['from']
        from_index = self.textToIndex(from_text)
        to_text = time_dict_input['time']['to']
        to_index = self.textToIndex(to_text)

        # Check to see if the event can be added
        canAdd = True

        for i in range(from_index, to_index):
            if self.schedule[day][i]:
                canAdd = False

        if canAdd:
            for i in range(from_index, to_index):
                self.schedule[day][i] = 1
            print('Successfully add this event into schedule')

        else:
            print('Failed to add this event because of existing events')
    
    
    def del_event(self, time_dict_input):
        
        day = time_dict_input['day']
        from_text = time_dict_input['time']['from']
        from_index = self.textToIndex(from_text)
        to_text = time_dict_input['time']['to']
        to_index = self.textToIndex(to_text)

        # Check to see if the event can be removed
        canRemove = True

        for i in range(from_index, to_index):
            if not self.schedule[day][i]:
                canRemove = False

        if canRemove:
            for i in range(from_index, to_index):
                self.schedule[day][i] = 0
            print('Successfully deleted this event from schedule')
            
        else:
            print('Failed to del this event because of the empty slots')
        
    def view_schedule(self):
        print(self.name)
        total = 0
        for i in self.schedule:
            print(f'\t{i}: {self.schedule[i]}')
            total += sum(self.schedule[i])
        print(f'Total available hours: {total/2}\n')
    

    def generateTimes(self, number, distance):

        for _ in range(10000): # Allowed to try 10k times
            nums = []
            candidates = list(range(0, nslots - distance + 1))
            random.shuffle(candidates)

            for x in candidates:
                if all(abs(x - y) >= distance for y in nums):
                    nums.append(x)
                    if len(nums) == number:
                        return sorted(nums)

    def textToIndex(self, text):
        split_string = text.split(':')
        temp = 2 * (int(split_string[0]) - startOfDay)
        if split_string[1] == '30':
            temp += 1
        return temp


if __name__ == '__main__':
    #self_testing region

    pass