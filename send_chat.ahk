msg := A_Args[1]

; Activate League window (optional)
WinActivate("League of Legends (TM) Client")

Send("{Enter}")
Sleep(100)
Send(msg)
Sleep(100)
Send("{Enter}")