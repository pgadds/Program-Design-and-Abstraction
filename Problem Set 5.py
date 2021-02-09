#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:50:13 2019

@author: navboi
"""
#Part1
class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)                 
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict        
        

    def apply_shift(self, shift):
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)
    
    #Part2
    class PlaintextMessage(Message):
        def __init__(self, text, shift):
       
            self.shift = shift
            self.message_text = text
            self.valid_words = load_words(WORDLIST_FILENAME)
            self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
            self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

        def get_shift(self):
        
            return self.shift

        def get_encrypting_dict(self):
            
            encrypting_dict_copy = self.encrypting_dict.copy()
            return encrypting_dict_copy

        def get_message_text_encrypted(self):
            
            return self.message_text_encrypted

        def change_shift(self, shift):
            
            self.shift = shift
            self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
            self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)
        
    #Part3
    class CiphertextMessage(Message):
        def __init__(self, text):
            self.message_text = text
            self.valid_words = load_words(WORDLIST_FILENAME)

        def decrypt_message(self):
            word_counter = 0
            max_count = 0
            for i in range(26):
                for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                    if is_word(self.valid_words, j):
                        word_counter += 1
                        if word_counter > max_count:
                            max_count = word_counter
                            shift_value = i
                            decrypted_msg = super(CiphertextMessage, self).apply_shift(i)
                        
                        return (shift_value, decrypted_msg)
    
    #Part4
        def decrypt_story():
            joke_code = CiphertextMessage(get_story_string())
            return joke_code.decrypt_message()
    