from tkinter import *
from run import predict

# valid 19
code1='public ImmutableIntArray subArray(int startIndex, int endIndex) {\n    Preconditions.checkPositionIndexes(startIndex, endIndex, length());\n    return startIndex == endIndex\n        ? EMPTY\n        : new ImmutableIntArray(array, start + startIndex, start + endIndex);\n  }'
print('\ncode1:')
print(code1)
# valid 1
code2='@CanIgnoreReturnValue\n  public long copyTo(CharSink sink) throws IOException {\n    checkNotNull(sink);\n\n    Closer closer = Closer.create();\n    try {\n      Reader reader = closer.register(openStream());\n      Writer writer = closer.register(sink.openStream());\n      return CharStreams.copy(reader, writer);\n    } catch (Throwable e) {\n      throw closer.rethrow(e);\n    } finally {\n      closer.close();\n    }\n  }'
print('\ncode2:')
print(code2)

root=Tk()
root.geometry('750x600')
root.title('Code Summarization')

label1=Label(root,text='Code Summarization',font=('Consolas',20))
label1.place(x=250,y=30)
label2=Label(root,text='Enter code below:',font=('Consolas',14))
label2.place(x=70,y=80)

text1=Text(root,width=90,height=18)
text1.place(x=55,y=110)
text2=Text(root,width=90,height=8)
text2.place(x=55,y=450)

def Print():
    text=text1.get(1.0,END)
    text=predict(text)
    text2.delete(1.0,END)
    text2.insert(1.0,text)

def Clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)

button1=Button(root,text='translate',font=('Consolas',14),width=30,height=2,command=Print)
button1.place(x=55,y=370)
button2=Button(root,text='clear',font=('Consolas',14),width=30,height=2,command=Clear)
button2.place(x=380,y=370)

root.mainloop()
