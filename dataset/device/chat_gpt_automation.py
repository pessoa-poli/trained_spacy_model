import undetected_chromedriver as uc 
from undetected_chromedriver import By
import time
import pyperclip # The name you have the file
from full_list import *

"""This script is an attempt to automate the ChatGPT Phrase Automation for the creation of a dataset"""

next_button_selector = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button > div"
next_button_selector2 = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-neutral.ml-auto > div"
done_button_selector = "#headlessui-dialog-panel-\:r1\: > div.prose.dark\:prose-invert > div.flex.gap-4.mt-6 > button.btn.relative.btn-primary.ml-auto > div"
textarea_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > textarea"
send_prompt_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.flex.h-full.flex-1.flex-col.md\:pl-\[260px\] > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button"
copy_code_button_selector = "button.flex"
new_chat_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > a.flex.py-3.px-3.items-center.gap-3.rounded-md.hover\:bg-gray-500\/10.transition-colors.duration-200.text-white.cursor-pointer.text-sm.mb-2.flex-shrink-0.border.border-white\/20"
bin_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > div > div > a.flex.py-3.px-3.items-center.gap-3.relative.rounded-md.cursor-pointer.break-all.pr-14.bg-gray-800.hover\:bg-gray-800.group.animate-flash > div.absolute.flex.right-1.z-10.text-gray-300.visible > button:nth-child(2)"
confirm_bin_button_selector = "#__next > div.overflow-hidden.w-full.h-full.relative > div.dark.hidden.bg-gray-900.md\:fixed.md\:inset-y-0.md\:flex.md\:w-\[260px\].md\:flex-col > div > div > nav > div > div > a.flex.py-3.px-3.items-center.gap-3.relative.rounded-md.cursor-pointer.break-all.pr-14.bg-gray-800.hover\:bg-gray-800.group.animate-flash > div.absolute.flex.right-1.z-10.text-gray-300.visible > button:nth-child(1)"

options = uc.ChromeOptions()
# options.headless = True 
driver = uc.Chrome(use_subprocess=True, options=options)
driver.get("https://chat.openai.com/auth/login") 
driver.maximize_window()
wait_on_input = input("Can I proceed?") # Wait for login preparations
# phrase = """Can you create a phrase with the string "Nest Learning Thermostat" ? The phrase must be a software requirement storyline. Output it as a python string."""

def buildString(word):
    return f"""Generate 20 sentences with the string "{word}"? The phrases must be slices of storylines used in system development. Give me the output inside a python code block."""

def createPhrase(somePrompt):
    # driver.find_element(By.CSS_SELECTOR,'button.btn:nth-child(1)').click()    
    driver.find_element(By.CSS_SELECTOR,textarea_selector).send_keys(somePrompt)
    driver.find_element(By.CSS_SELECTOR,send_prompt_button_selector).click()
    time.sleep(50)
    driver.find_element(By.CSS_SELECTOR,copy_code_button_selector).click()
    driver.find_element(By.CSS_SELECTOR,bin_button_selector).click()
    driver.find_element(By.CSS_SELECTOR,confirm_bin_button_selector).click()
    #driver.save_screenshot("gpty.png")
    answer = pyperclip.paste()
    with open("./output_device_phrases.txt", "a+") as f:
        f.write(answer)
    # print(30*"#")
    # print(answer)
    # print(30*"#")


if __name__ == "__main__":
    for i in range(3):
        myPrompt = buildString(full_list[i])
        print(myPrompt)
        createPhrase(myPrompt)
    wait_on_input = input("Can I finish?")
    driver.close()
