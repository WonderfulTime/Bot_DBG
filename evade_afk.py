import time
import numpy as np
import win32com.client as win32
import win32api, win32con
import cv2
from PIL import ImageGrab
import imgutils
import easyocr
from matplotlib import pyplot as pl
from mss import mss

import argparse
import pyautogui
from time import sleep
from matplotlib import pyplot as pltd
from termcolor import colored

def evade_afk_check():
    afk_choose_screen = ImageGrab.grab(bbox=(440, 152, 1465, 378))  # область АФК CHOOSE
    afk_choose_screen.save('image/DBG/Screens/screen_afk.jpeg')

    img_grb_afk = cv2.imread('image/DBG/Screens/screen_afk.jpeg')
    img_gray_afk = cv2.cvtColor(img_grb_afk, cv2.COLOR_BGR2GRAY)

    text = easyocr.Reader(['en'])

    textAFK = text.readtext(img_gray_afk, detail=0, paragraph=True)
    new_text_AFK = str(textAFK)

    print(new_text_AFK)

    while "Select" in new_text_AFK:  # проверка на найденное значение в кортеже
        print("choose item")
        q = new_text_AFK.find("Select")
        print(q)

        # подставить выбор итемов АФК

        # начало афк проверки итемов
        select_itm = cv2.imread('image/DBG/afk/screen_afk.jpeg')

        # сюда вставлять участок кода проверок

        item_screen = ImageGrab.grab(bbox=(61, 42, 1822, 1026))  # область АФК Circle
        item_screen.save('image/DBG/Screens/item_screen.jpeg')

        img_grb_afk = cv2.imread('image/DBG/Screens/item_screen.jpeg')
        img_gray_afk = cv2.cvtColor(img_grb_afk, cv2.COLOR_BGR2GRAY)
        #
        ### проверка условий на совпадение текста и картинки и клик на нее

        if "47" in new_text_AFK:
            item = "AK-47"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Axe" in new_text_AFK:
            item = "Axe"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)
        #
        elif "Beginner Sword" in new_text_AFK:
            item = "Beginner Sword"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Boomerang" in new_text_AFK:
            item = "Boomerang"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Brown Fedora" in new_text_AFK:
            item = "Brown Fedora"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Cheap Headphones" in new_text_AFK:
            item = "Cheap Headphones"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Cleaver" in new_text_AFK:
            item = "Cleaver"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Cowboy Hat" in new_text_AFK:
            item = "Cowboy Hat"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Crimson Bow" in new_text_AFK:
            item = "Crimson Bow"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Fez" in new_text_AFK:
            item = "Fez"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Glock" in new_text_AFK:
            item = "Glock"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Graduation Cap" in new_text_AFK:
            item = "Graduation Cap"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Hard Hat" in new_text_AFK:
            item = "Hard Hat"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Kunai" in new_text_AFK:
            item = "Kunai"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Longsword" in new_text_AFK:
            item = "Longsword"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Hakeshift Bow" in new_text_AFK:
            item = "Makeshift Bow"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Pickaxe" in new_text_AFK:
            item = "Pickaxe"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Propeller Cap" in new_text_AFK:
            item = "Propeller Cap"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Reading Glasses" in new_text_AFK:
            item = "Reading Glasses"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Shuriken" in new_text_AFK:
            item = "Shuriken"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Strawberry Cone" in new_text_AFK:
            item = "Strawberry Cone"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Surgical Nask" in new_text_AFK:
            item = "Surgical Mask"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        elif "Top Hat" in new_text_AFK:
            item = "Top Hat"

            item_template = cv2.imread(
                'image/DBG/Cut/last_changed/' + item + '.png')
            img_screen_afc_grb = cv2.imread(
                'image/DBG/Screens/item_screen.jpeg')

            w = item_template.shape[1]
            h = item_template.shape[0]

            result = cv2.matchTemplate(img_screen_afc_grb, item_template, cv2.TM_CCOEFF_NORMED)
            th = 0.93
            loc = np.where(result >= th)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(img_screen_afc_grb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

            # попытка клика на верное изображение
            try:
                x = (pt[
                         0] + w + 30)  # прибалять разницу к координатам между обрезанным скрином и полным экраном
                y = (pt[1] + h + 30)
                pyautogui.click(x, y)
                # клик

                print("DONEEE")

            except:
                print("Значение изображения не в том диапазоне")

            sleep(1)

        else:
            pyautogui.click(100, 100)

        ###

        # конец участка кода

        # if "Suspicious Goggles" in new_text_AFK:
        #
        #     #проверка картинок
        #     #надо узнать точное имя картинки
        #     # current_item = np.where( = items_name[0])
        #     print("DONEEE")
        #     #
        # else:
        #
        #     #клик в первый объект для смены пула
        #     pyautogui.moveTo(256, 526)  #реролл
        #     pyautogui.click()

        # конец афк проверки итемов

        sleep(2)

        # обновление картинки для цикла
        afk_choose_screen = ImageGrab.grab(bbox=(440, 152, 1465, 378))  # область АФК CHOOSE
        afk_choose_screen.save('image/DBG/Screens/screen_afk.jpeg')

        img_grb_afk = cv2.imread('image/DBG/Screens/screen_afk.jpeg')
        img_gray_afk = cv2.cvtColor(img_grb_afk, cv2.COLOR_BGR2GRAY)

        text = easyocr.Reader(['en'])

        textAFK = text.readtext(img_gray_afk, detail=0, paragraph=True)
        new_text_AFK = str(textAFK)



    else:
        print("Has no AFK_Items")

    sleep(2)

    # проверка на АФК Circle
    # def afk_circle(): #захват области circle и чтение кортежа с Tap!

    afk_Circle_choose_screen = ImageGrab.grab(bbox=(61, 42, 1822, 1026))  # область АФК Circle
    afk_Circle_choose_screen.save(
        'image/DBG/Screens/screen_afk_circle.jpeg')

    img_grb_afk = cv2.imread(
        'image/DBG/Screens/screen_afk_circle.jpeg')
    img_gray_afk = cv2.cvtColor(img_grb_afk, cv2.COLOR_BGR2GRAY)

    text = easyocr.Reader(['en'])

    textAFK = text.readtext(img_gray_afk, detail=0, paragraph=True)
    new_text_AFK = str(textAFK)

    while ("Tap" or "Tapl" or "Tap!" or "Tapx" or "Tani" or "Tan|") in new_text_AFK:
        print("click the circles")

        one_cycle = 0
        for one_cycle in range(1):
            # нажатие на кружки и наводка

            # Поиск цвета на экране
            def find_color(our_color, monitor={}):

                # Возмём кусок экрана

                m = mss()
                # Получаем пиксель с экрана монитора
                img = m.grab(monitor)

                # Преобразуем этот пиксель в матрицу
                img_arr = np.array(img)

                # Поиск цвета (b, g, r, alpha)
                our_map = (our_color[2], our_color[1], our_color[0], 255)
                indexes = np.where(np.all(img_arr == our_map, axis=-1))
                our_crd = np.transpose(indexes)

                return our_crd

            # Искомый цвет
            our_color1_1 = [26, 98, 11]  # зеленый
            our_color1_2 = [25, 101, 10]
            our_color1_3 = [6, 123, 2]
            our_color1_4 = [6, 117, 7]
            our_color1_5 = [4, 130, 4]
            our_color1_6 = [3, 130, 6]
            our_color1_7 = [25, 142, 22]
            our_color1_8 = [3, 129, 17]
            our_color1_9 = [5, 131, 6]
            our_color1_10 = [0, 122, 0]

            ####

            our_color2_1 = [128, 12, 8]  # красный
            our_color2_2 = [159, 10, 6]
            our_color2_3 = [166, 0, 0]
            our_color2_4 = [169, 6, 5]
            our_color2_5 = [170, 6, 7]
            our_color2_6 = [118, 11, 12]
            our_color2_7 = [173, 6, 7]
            our_color2_8 = [173, 7, 5]
            our_color2_9 = [117, 13, 9]
            our_color2_10 = [155, 8, 6]

            #####

            our_color3_1 = [151, 113, 10]  # желтый
            our_color3_2 = [174, 126, 6]
            our_color3_3 = [154, 113, 1]
            our_color3_4 = [158, 119, 9]
            our_color3_5 = [105, 87, 9]
            our_color3_6 = [132, 104, 8]
            our_color3_7 = [157, 117, 8]
            our_color3_8 = [155, 116, 8]
            our_color3_9 = [133, 106, 15]
            our_color3_10 = [177, 128, 9]

            #######

            result = find_color(our_color1_1, monitor)  # первая проверка по цвету зеленый

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_2, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_3, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_4, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_5, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_6, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_7, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_8, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_9, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color1_10, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            ###########

            # вторая проверка по цвету красный

            result = find_color(our_color2_1, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_2, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_3, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_4, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_5, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_6, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_7, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_8, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_9, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color2_10, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            ##########

            # третья проверка по цвету желтый

            result = find_color(our_color3_1, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_2, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_3, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_4, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_5, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_6, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_7, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_8, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_9, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            result = find_color(our_color3_10, monitor)

            if result.__len__():
                x = result[0][1] + monitor.get('left')
                y = result[0][0] + monitor.get('top')

                pyautogui.click(x, y)  # заменить на клик
                time.sleep(1)

            one_cycle = (one_cycle + 1)

        # break

        # threshold
        # if max_val >= 0.8:
        #  pyautogui.click(
        #     x = max_loc[0] + x, #screen x
        #     y = max_loc[1] + y  #screen y
        #  )

        # new_text_AFK = None #очистка переменной текста проверки while

        # конструкция проверки АФК кружков
        afk_Circle_choose_screen = ImageGrab.grab(bbox=(61, 42, 1822, 1026))  # область АФК Circle
        afk_Circle_choose_screen.save(
            'image/DBG/Screens/screen_afk_circle.jpeg')

        img_grb_afk = cv2.imread(
            'image/DBG/Screens/screen_afk_circle.jpeg')
        img_gray_afk = cv2.cvtColor(img_grb_afk, cv2.COLOR_BGR2GRAY)

        text = easyocr.Reader(['en'])

        textAFK = text.readtext(img_gray_afk, detail=0, paragraph=True)
        new_text_AFK = str(textAFK)

        sleep(0.2)