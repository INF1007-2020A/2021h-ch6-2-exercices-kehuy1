#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    dictionnaire = {}
    for index in range(len(some_list)):
        dictionnaire[some_list[index]] = index
    return dictionnaire


def color_name_to_hex(colors: list) -> list:
    new_list = []
    for element in colors:
        new_list.append((element, cnames[element]))

    return new_list


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    list = []
    for num in range(0, 10000):
        if num < 15 or num > 350:
            list.append(num)

    return list


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    liste_nom_modele = list(model_dict.keys())
    liste_valeurs_modele = list(model_dict.values())
    dictionnaire_modele = {}
    moy = 0

    for first_element in range(len(liste_valeurs_modele)):
        for second_element in range(len(liste_valeurs_modele[first_element])):
            moy += ((liste_valeurs_modele[first_element][second_element][0] - liste_valeurs_modele[first_element][second_element][1])**2) / len(liste_valeurs_modele[first_element])

        dictionnaire_modele[liste_nom_modele[first_element]] = moy
        moy = 0



    return dictionnaire_modele


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
