; open new tab in firefox
#t::
SetTitleMatchMode, 2
If WinExist ("ahk_exe firefox.exe") {
	WinActivate, ahk_exe firefox.exe
	WinWaitActive, ahk_exe firefox.exe
	Send ^t
}
return

; screenshot
#b::
Send #+s
return

; maximize current window
#+f::
Send #{Up}
return

; close current window
#q::
Send !{F4}
return



; list of all windows (unique)
^q::
WinGet, WinList, List,,, Program Manager
List = 
Loop, %WinList% {
	Current := WinList%A_Index%
	WinGetTitle, WinTitle, ahk_id %Current%
	
	If WinTitle AND !InStr(List, WinTitle) {
		List .= "`n" WinTitle
	}
}
MsgBox %List%
return



; snap all windows (mvp 😂)
^q::
WinGet, WinList, List,,, Program Manager
arr := []
Loop, %WinList% {
	arr.Push(WinList%A_Index%)
}

len := arr.Length()
Loop, %len% {
	id := arr[A_Index]
	Loop %A_Index% {
		WinActivate, ahk_id %id%
		WinWaitActive, ahk_id %id%
		Send #{Right}
	}
}
Return
