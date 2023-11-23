import threading

import customtkinter as ctk
import discord
from discord import Webhook
import asyncio
import aiohttp

app = ctk.CTk()

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# App Settings
app.title("CxWebhookSpam")
app.geometry("500x650")
app.resizable(height=False, width=False)
app.font = ctk.CTkFont(size=50)

embedV = ctk.StringVar(value="0")

logTFrame = ctk.CTkFrame(app, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30,
                         fg_color='transparent')
logTFrame.pack()

logT = ctk.CTkLabel(logTFrame, text="[Log]")
logT.pack(padx=30, pady=5)


def runThread():
    threading.Thread(target=sendToWebhook).start()


def sendToWebhook():
    try:
        async def anything(webhook2):
            async with aiohttp.ClientSession() as session:
                message = MessageE.get()
                times = int(TimesE.get())
                user = UserE.get()
                numBr = 1
                for i in range(times):
                    numBr = numBr + 1
                    webhook = Webhook.from_url(webhook2, session=session)
                    if embedV.get() == "1":
                        embed = discord.Embed(
                            title=message)
                        await webhook.send(embed=embed, username=user, avatar_url="https://cdn.discordapp.com/attachments/920941140528758824/1168336306393329774/togif-1.gif?ex=655164fa&is=653eeffa&hm=fb8ae844ae5397305f6890ff54f55c8904873680b7627f4c307716785826f6f4&")
                    else:
                        await webhook.send(username=user, content=message, avatar_url="https://cdn.discordapp.com/attachments/920941140528758824/1168336306393329774/togif-1.gif?ex=655164fa&is=653eeffa&hm=fb8ae844ae5397305f6890ff54f55c8904873680b7627f4c307716785826f6f4&")
                    logT.configure(text=f"Send Message [Remaining: {str(numBr)}/{str(times)}", text_color="green")

        webhook2 = tokenE.get()

        loop = asyncio.new_event_loop()
        loop.run_until_complete(anything(webhook2))
        loop.close()
        logT.configure(text=f"Done", text_color="magenta")
    except:
        logT.configure(text=f"Error Sending Message [Error Happened", text_color="red")


MainAFrame = ctk.CTkFrame(app, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainAFrame.pack(pady=50)

mainLable = ctk.CTkLabel(MainAFrame, text="CxMessageSpam", font=app.font)
mainLable.pack(pady=30)

MainBFrame = ctk.CTkFrame(app, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainBFrame.pack(pady=10)

# Token Input
tokenE = ctk.CTkEntry(MainBFrame, placeholder_text="Enter Webhook", height=38, font=("Trebuchet MS", 30),
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "grey"), width=400, fg_color='transparent')
tokenE.pack(padx=20, pady=10)

# Message Input
MessageE = ctk.CTkEntry(MainBFrame, placeholder_text="Enter Message To Spam", height=38, font=("Trebuchet MS", 30),
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "grey"), width=400, fg_color='transparent')
MessageE.pack(padx=20, pady=10)

# Message Input
TimesE = ctk.CTkEntry(MainBFrame, placeholder_text="How Many Times?", height=38, font=("Trebuchet MS", 30),
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "grey"), width=400, fg_color='transparent')
TimesE.pack(padx=20, pady=10)

# Message Input
UserE = ctk.CTkEntry(MainBFrame, placeholder_text="User Name", height=38, font=("Trebuchet MS", 30),
                     text_color="white",
                     border_width=1, border_color=("#00ffd0", "grey"), width=400, fg_color='transparent')
UserE.pack(padx=20, pady=10)

embedS = ctk.CTkSwitch(MainBFrame, text="Send As Embed", variable=embedV, onvalue="1", offvalue="0",
                       progress_color="#960325")
embedS.pack(padx=20, pady=5)

# Start
StartButton = ctk.CTkButton(app, text="Start Spamming", border_width=1,
                            border_color=("#0062ff", "#00876e"), fg_color='transparent', hover_color="#00876e",
                            font=("Trebuchet MS", 30), text_color="white", command=runThread)
StartButton.pack(pady=10)

app.mainloop()
