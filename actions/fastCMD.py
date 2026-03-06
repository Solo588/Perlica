'''
    codes that runs the fast response CMD
'''

def cmd(text):
    if text.lower() == "commands":
                    await message.reply_text(
                        "status - check public status\n"
                        "make public/private - toggle option\n" 
                        "health - computer health\n"
                        "kill - turn off\n"
                        "menti spam (code), (times)")
                    print(event)
                    return

        elif text.lower() == "status":
            await message.reply_text(f"Public: {public}")
            print(event)
            return

        elif text.lower() == "make public":
            if public:
                await message.reply_text("Perlica is already public")
            else: 
                public = True
                await message.reply_text("Perlica made public")
            return

        elif text.lower() == "make private":
            if not public:
                await message.reply_text("Perlica is already private")
            else:  
                public = False
                await message.reply_text("Perlica made private")
            return

        elif text.lower() == "kill":
            await message.reply_text("perlica shutting down.")
            await context.application.stop()
            print (event)
            print ("Perlica shutted down.")
            return