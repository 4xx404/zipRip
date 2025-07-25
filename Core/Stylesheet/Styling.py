#!/usr/bin/python3
# -*- coding: utf-8 -*-

class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'
	
class sd:
	iBan = f"{bc.BC} [{bc.GC}?{bc.BC}]" # Info banner
	sBan = f"{bc.BC} [{bc.GC}" + u'\u2713' + f"{bc.BC}]" # Success banner
	eBan = f"{bc.BC} [{bc.RC}" + u'\u2717' + f"{bc.BC}]" # Error banner
	
class Banner:
    Author = f"{bc.BC}\n Author:{bc.GC} 4xx404 \n"
    Version = f"{bc.BC} Version:{bc.GC} 1.0 \n"
    Github = f"{bc.BC} Github: {bc.GC}https://github.com/4xx404 \n"
	
    Logo = rf"""{bc.RC}
                (                
{bc.GC}                )\ )             
{bc.BC}     (         (()/( (           
{bc.RC}  (  )\   ) )   )(_)))\   ) )    
{bc.GC}  )\((_) /(/(  (_)) ((_) /(/(    
{bc.BC} ((_)(_)((_)_\ | _ \ (_)((_)_\   
{bc.RC} |_ /| || '_ \)|   / | || '_ \)  
{bc.GC} /__||_|| .__/ |_|_\ |_|| .__/   
{bc.BC}        |_|             |_|      
{Author}{Version}{Github}"""