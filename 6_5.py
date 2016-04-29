text = "X-DSPAM-Confidence:    0.8475";
sub_text = float(text[text.find('0'):len(text)])
print sub_text