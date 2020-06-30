#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 30, 2020, at 18:19
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'sAdaptAlpha2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'taskVer': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\sAdaptAlpha2\\sAdaptAlpha2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "s"
sClock = core.Clock()
counter = 0

# Initialize components for Routine "s2"
s2Clock = core.Clock()
# Do error checking for correct values of taskVer
try:
    taskVer = int(expInfo['taskVer']) # Check to see if this is safe
except ValueError:
    taskVer = 0

# Variables to keep track of the order, rotation and target choices
orderChoice = taskVer % 6
rotationChoice = np.floor( taskVer / 12 ) % 2
targetChoice = np.floor( taskVer / 6) % 2

# Order 
order = [0,1] # Default choice
if (orderChoice == 0):
    order = [0,1]
elif (orderChoice == 1):
    order = [0,2]
elif (orderChoice == 2):
    order = [1,0]
elif (orderChoice == 3):
    order = [1,2]
elif (orderChoice == 4):
    order = [2,0]
elif (orderChoice == 5):
    order = [2,1]


# Rotation of the mouse angle
rotation = [1,-1] # Default choice
if (rotationChoice == 0):
    rotation = [1,-1]
elif (rotationChoice == 1):
    rotation = [-1,1]

# Choose set of angles for Main and Inverted task, respectively
targetAngles = [[40,50],[130,140]] # Default choice
if (targetChoice == 0):
    targetAngles = [[40,50],[130,140]]
elif (targetChoice == 1):
    targetAngles = [[130,140],[40,50]]


# Initialize components for Routine "i"
iClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='Move mouse. Space countinue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrResp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
ang = None
rtd = None

#Set up rotations and main tasks
# NOTE: JS isn't automatically converted with global keyword
def setAbruptMainTask():
    print('Abrupt Main Task')
    ang = rotation[0] * 30
    rtd = ang*(pi/180)

def setRampedMainTask():
    print('Ramped Main Task')
    if (trials2.thisN <= 47):
        ang = rotation[0] * (trials2.thisN+1)*0.625
    else:
        ang = rotation[0] * 30
    rtd = ang*(pi/180)

def setStepMainTask():
    print('Step Main Task')
    if (trials2.thisN <= 23):
        ang = rotation[0] * 7.5
    elif (trials2.thisN > 23 and trials2.thisN <= 47):
        ang = rotation[0] * 15
    elif (trials2.thisN > 47 and trials2.thisN <= 71):
        ang = rotation[0] * 22.5
    else:
        ang = rotation[0] * 30
    rtd = ang*(pi/180)

#Set up inverses
# Might be possible combine these with the Main task functions
def setAbruptInverseTask():
    print('Abrupt Inverse Task')
    ang = rotation[1] * 30
    rtd = ang*(pi/180)

def setRampedInverseTask():
    print('Ramped Inverse Task')
    if (trials2.thisN <= 47):
        ang = rotation[1] * (trials2.thisN+1)*0.625
    else:
        ang = rotation[1] * 30
    rtd = ang*(pi/180)

def setStepInverseTask():
    print('Step Inverse Task')
    if (trials2.thisN <= 23):
        ang = rotation[1] * 7.5
    elif (trials2.thisN > 23 and trials2.thisN <= 47):
        ang = rotation[1] * 15
    elif (trials2.thisN > 47 and trials2.thisN <= 71):
        ang = rotation[1] * 22.5
    else:
        ang = rotation[1] * 30
    rtd = ang*(pi/180)

trialTarget = visual.Polygon(
    win=win, name='trialTarget',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trialHome = visual.Polygon(
    win=win, name='trialHome',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trialCursor = visual.Polygon(
    win=win, name='trialCursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trialStep
trialStep = 0
trialStepContainer = []
trialNum = visual.TextStim(win=win, name='trialNum',
    text='0',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trialSkip = keyboard.Keyboard()

# Initialize components for Routine "e"
eClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Space exit',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "s"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
sComponents = []
for thisComponent in sComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "s"-------
while continueRoutine:
    # get current time
    t = sClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "s"-------
for thisComponent in sComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "s" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
selectLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('selectionVariables.xlsx'),
    seed=None, name='selectLoop')
thisExp.addLoop(selectLoop)  # add the loop to the experiment
thisSelectLoop = selectLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSelectLoop.rgb)
if thisSelectLoop != None:
    for paramName in thisSelectLoop:
        exec('{} = thisSelectLoop[paramName]'.format(paramName))

for thisSelectLoop in selectLoop:
    currentLoop = selectLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSelectLoop.rgb)
    if thisSelectLoop != None:
        for paramName in thisSelectLoop:
            exec('{} = thisSelectLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "s2"-------
    continueRoutine = True
    # update component parameters for each repeat
    counter = counter + 1
    loopCount = int(loopCount) # convert the loopCount in selectionLoop to an int
    # keep track of which components have finished
    s2Components = []
    for thisComponent in s2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    s2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "s2"-------
    while continueRoutine:
        # get current time
        t = s2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=s2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in s2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "s2"-------
    for thisComponent in s2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "s2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=repRows, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('selectionRows.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "i"-------
        continueRoutine = True
        # update component parameters for each repeat
        instrResp.keys = []
        instrResp.rt = []
        _instrResp_allKeys = []
        if not(counter == 3 or counter == 7):
            continue
            
        if counter == 3:
            instr.text = "Move mouse. Space countinue."
            
        if counter == 7:
            instr.text = "Move mouse. Space countinue."
            
        # keep track of which components have finished
        iComponents = [instr, instrResp]
        for thisComponent in iComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        iClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "i"-------
        while continueRoutine:
            # get current time
            t = iClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=iClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instr* updates
            if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instr.frameNStart = frameN  # exact frame index
                instr.tStart = t  # local t and not account for scr refresh
                instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
                instr.setAutoDraw(True)
            
            # *instrResp* updates
            waitOnFlip = False
            if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instrResp.frameNStart = frameN  # exact frame index
                instrResp.tStart = t  # local t and not account for scr refresh
                instrResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
                instrResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if instrResp.status == STARTED and not waitOnFlip:
                theseKeys = instrResp.getKeys(keyList=['space'], waitRelease=False)
                _instrResp_allKeys.extend(theseKeys)
                if len(_instrResp_allKeys):
                    instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                    instrResp.rt = _instrResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in iComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "i"-------
        for thisComponent in iComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('instr.started', instr.tStartRefresh)
        trials.addData('instr.stopped', instr.tStopRefresh)
        # the Routine "i" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trialMouse
        trialMouse.x = []
        trialMouse.y = []
        trialMouse.leftButton = []
        trialMouse.midButton = []
        trialMouse.rightButton = []
        trialMouse.time = []
        gotValidClick = False  # until a click is received
        trialMouse.mouseClock.reset()
        win.mouseVisible = False
        
        targetangle = targetAngles[loopCount][trials.thisN % 2] # targetAngles defined in instruction1
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        screen_width = win.size[0]/win.size[1]
        screen_height = win.size[1]/win.size[1]
        
        trimmed_width = (2/3) * screen_width
        trimmed_height = (2/3) * screen_height
        
        if trimmed_height*2 < trimmed_width:
            trimmed_width = trimmed_height*2
        else:
            trimmed_height = trimmed_width/2
        
        homePos = [0, -0.35 * trimmed_height]
        
        targetOpacity = 0
        homeOpacity = 0
        #'buffer' circle set up
        bufferOpacity = 0
        bufferRadius = (sqrt(trial4Cursor.pos[0]**2 + trial4Cursor.pos[1]**2))
        #allows cursor opacity changing
        cursorOpacity = 1
        cursorPosX = trialCursor.pos[0]
        CursorPosY = trialCursor.pos[1] 
        
        homeStart = False
        reachOut = False
        
        trialStep = 1
        steps = []
        
        if counter == 1:
            print("Align task")
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 12'
            
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
            
        if counter == 2:
            print('Error Clamped Task')
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 12'
        
            cursorOpacity = 0
        
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
        
            theta = (targetangle / 180) * pi
        
        if counter == 3 or counter == 7:
            print("Align task")
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 32'
        
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
            
        if counter == 4 or counter == 8:
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 96'
        
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
        
            task = order[loopCount] # loopCount taken from the selectionVariables.xlsx
        
            if (task == 0):
                setAbruptMainTask()
            elif (task == 1):
                setRampedMainTask()
            elif (task == 2):
                setStepMainTask()
            else:
                setAbruptMainTask() # Contingency condition don't know if this is needed
        
            trialText.text = str(ang)
            
        if counter == 5 or counter == 9:
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 8'
        
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
        
            task = order[loopCount]
        
            if (task == 0):
                setAbruptInverseTask()
            elif (task == 1):
                setRampedInverseTask()
            elif (task == 2):
                setStepInverseTask()
            else:
                setAbruptInverseTask() # Contingency condition don't know if this is needed
                    
            trialText.text = str(ang)
            
        if counter == 6 or counter == 10:
            #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
            trialNum.text = str(trials.thisN+1)+' / 24'
        
            trialCursor.pos = (1.5,1.5)
            trialMouse.pos = (1.5,1.5)
        
            cursorOpacity = 0
        
            theta = (targetangle / 180) * pi
        
            print('Error Clamped Task')
        trialSkip.keys = []
        trialSkip.rt = []
        _trialSkip_allKeys = []
        # keep track of which components have finished
        trialComponents = [trialMouse, trialTarget, trialHome, trialCursor, trialNum, trialSkip]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *trialMouse* updates
            if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMouse.frameNStart = frameN  # exact frame index
                trialMouse.tStart = t  # local t and not account for scr refresh
                trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
                trialMouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trialMouse.status == STARTED:  # only update if started and not finished!
                x, y = trialMouse.getPos()
                trialMouse.x.append(x)
                trialMouse.y.append(y)
                buttons = trialMouse.getPressed()
                trialMouse.leftButton.append(buttons[0])
                trialMouse.midButton.append(buttons[1])
                trialMouse.rightButton.append(buttons[2])
                trialMouse.time.append(trialMouse.mouseClock.getTime())
            CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget.pos[0])**2 + (trialCursor.pos[1]-trialTarget.pos[1])**2)
            CursorHomeDistance = sqrt(trialCursor.pos[0]**2 + trialCursor.pos[1]**2)
            
            steps.append(trialStep)
            # steps.push(step)
            
            if counter == 1:
                cursorPosX = trialCursor.pos[0]
                CursorPosY = trialCursor.pos[1]
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    if (CursorHomeDistance < .05):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trialStep = 2
                    if (CursorTargetDistance < .05):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 3
                    if (CursorHomeDistance < .05):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
                
            if counter == 2:
                cursorPosX = sqrt((trial4Mouse.getPos()[0]**2)+(trial4Mouse.getPos()[1]**2))*(cos(theta))
                CursorPosY = sqrt((trial4Mouse.getPos()[0]**2)+(trial4Mouse.getPos()[1]**2))*(sin(theta))
            
                if step == 2: 
                    theta = (targetangle / 180) * pi
                    rx = dist * cos(theta)
                    ry = dist * sin(theta)
                    radius = 1
                else:
                    if dist > 1:
                        rx = homex
                        ry = homey
                        radius = dist
                        diameter = 2*dist
                    else:
                        rx = xmouse
                        ry = ymouse
                        radius = 1
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    bufferOpacity = 0
                    cursorOpacity = 1
                    if (CursorHomeDistance < .075):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trialStep = 2
                    bufferOpacity = 0
                    cursorOpacity = 1
                    if (CursorTargetDistance < .025):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 3
                    #COntrols the 'buffer'
                    bufferOpacity = 1
                    bufferRadius = (sqrt(trialCursor.pos[0]**2 + trialCursor.pos[1]**2))
                    #controls the cursor
                    cursorOpacity = 0
                    if (CursorHomeDistance < .2):
                        cursorOpacity = 1
                    if (CursorHomeDistance < .075):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
            
            if counter == 3 or counter == 7:
                cursorPosX = trialCursor.pos[0]
                CursorPosY = trialCursor.pos[1]
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    if (CursorHomeDistance < .05):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trialStep = 2
                    if (CursorTargetDistance < .05):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 3
                    if (CursorHomeDistance < .05):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
                
            if counter == 4 or counter == 8:
                cursorPosX = (trialMouse.getPos()[0]*cos(rtd))-(trialMouse.getPos()[1]*sin(rtd))
                CursorPosY = (trialMouse.getPos()[0]*sin(rtd))+(trialMouse.getPos()[1]*cos(rtd))
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    if (CursorHomeDistance < .05):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trialStep = 2
                    if (CursorTargetDistance < .05):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 3
                    if (CursorHomeDistance < .05):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
                
            if counter == 5 or counter == 9:
                cursorPosX = (trialMouse.getPos()[0]*cos(rtd))-(trialMouse.getPos()[1]*sin(rtd))
                CursorPosY = (trialMouse.getPos()[0]*sin(rtd))+(trialMouse.getPos()[1]*cos(rtd))
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    if (CursorHomeDistance < .025):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trialStep = 2
                    if (CursorTargetDistance < .025):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 3
                    if (CursorHomeDistance < .025):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
                
            if counter == 6 or counter == 10:
                CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget.pos[0])**2 + (trialCursor.pos[1]-trialTarget.pos[1])**2)
                CursorHomeDistance = sqrt(trialCursor.pos[0]**2 + trialCursor.pos[1]**2)
                cursorPosX = sqrt((trialMouse.getPos()[0]**2)+(trialMouse.getPos()[1]**2))*(cos(theta))
                CursorPosY = sqrt((trialMouse.getPos()[0]**2)+(trialMouse.getPos()[1]**2))*(sin(theta))
            
                if step == 2: 
                    theta = (targetangle / 180) * pi
                    rx = dist * cos(theta)
                    ry = dist * sin(theta)
                    radius = 1
                else:
                    if dist > 1:
                        rx = homex
                        ry = homey
                        radius = dist
                        diameter = 2*dist
                    else:
                        rx = xmouse
                        ry = ymouse
                        radius = 1
            
                if not(homeStart):
                    homeOpacity = 1
                    targetOpacity = 0
                    trialStep = 1
                    bufferOpacity = 0
                    cursorOpacity = 1
                    if (CursorHomeDistance < .075):
                        homeStart = True
                        print('end step 1'+' ('+str(globalClock.getTime())+')')
            
                if (not(reachOut) and homeStart):
                    homeOpacity = 0
                    targetOpacity = 1
                    trial4Step = 2
                    bufferOpacity = 0
                    cursorOpacity = 1
                    if (CursorTargetDistance < .025):
                        reachOut = True
                        print('end step 2'+' ('+str(globalClock.getTime())+')')
            
                if (reachOut):
                    homeOpacity = 1
                    targetOpacity = 0
                    trial4Step = 3
                    #COntrols the 'buffer'
                    bufferOpacity = 1
                    bufferRadius = (sqrt(trial4Cursor.pos[0]**2 + trial4Cursor.pos[1]**2))
                    #controls the cursor
                    cursorOpacity = 0
                    if (CursorHomeDistance < .2):
                        cursorOpacity = 1
                    if (CursorHomeDistance < .075):
                        # maybe this ends the loop prematurely?
                        print('end step 3'+' ('+str(globalClock.getTime())+')')
                        continueRoutine = False
                        
                #steps = steps.append(step)
            
            
            
            # *trialTarget* updates
            if trialTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget.frameNStart = frameN  # exact frame index
                trialTarget.tStart = t  # local t and not account for scr refresh
                trialTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget, 'tStartRefresh')  # time at next scr refresh
                trialTarget.setAutoDraw(True)
            if trialTarget.status == STARTED:  # only update if drawing
                trialTarget.setOpacity(targetOpacity, log=False)
                trialTarget.setPos(targetPos, log=False)
            
            # *trialHome* updates
            if trialHome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialHome.frameNStart = frameN  # exact frame index
                trialHome.tStart = t  # local t and not account for scr refresh
                trialHome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialHome, 'tStartRefresh')  # time at next scr refresh
                trialHome.setAutoDraw(True)
            if trialHome.status == STARTED:  # only update if drawing
                trialHome.setOpacity(homeOpacity, log=False)
                trialHome.setPos(homePos, log=False)
            
            # *trialCursor* updates
            if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCursor.frameNStart = frameN  # exact frame index
                trialCursor.tStart = t  # local t and not account for scr refresh
                trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
                trialCursor.setAutoDraw(True)
            if trialCursor.status == STARTED:  # only update if drawing
                trialCursor.setOpacity(cursorOpacity, log=False)
                trialCursor.setPos([mousePosX, mousePosY], log=False)
            
            # *trialNum* updates
            if trialNum.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialNum.frameNStart = frameN  # exact frame index
                trialNum.tStart = t  # local t and not account for scr refresh
                trialNum.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialNum, 'tStartRefresh')  # time at next scr refresh
                trialNum.setAutoDraw(True)
            
            # *trialSkip* updates
            waitOnFlip = False
            if trialSkip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialSkip.frameNStart = frameN  # exact frame index
                trialSkip.tStart = t  # local t and not account for scr refresh
                trialSkip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialSkip, 'tStartRefresh')  # time at next scr refresh
                trialSkip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialSkip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialSkip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialSkip.status == STARTED and not waitOnFlip:
                theseKeys = trialSkip.getKeys(keyList=['space'], waitRelease=False)
                _trialSkip_allKeys.extend(theseKeys)
                if len(_trialSkip_allKeys):
                    trialSkip.keys = _trialSkip_allKeys[-1].name  # just the last key pressed
                    trialSkip.rt = _trialSkip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials (TrialHandler)
        trials.addData('trialMouse.x', trialMouse.x)
        trials.addData('trialMouse.y', trialMouse.y)
        trials.addData('trialMouse.leftButton', trialMouse.leftButton)
        trials.addData('trialMouse.midButton', trialMouse.midButton)
        trials.addData('trialMouse.rightButton', trialMouse.rightButton)
        trials.addData('trialMouse.time', trialMouse.time)
        trials.addData('trialMouse.started', trialMouse.tStartRefresh)
        trials.addData('trialMouse.stopped', trialMouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trials.addData('trialTarget.started', trialTarget.tStartRefresh)
        trials.addData('trialTarget.stopped', trialTarget.tStopRefresh)
        trials.addData('trialHome.started', trialHome.tStartRefresh)
        trials.addData('trialHome.stopped', trialHome.tStopRefresh)
        trials.addData('trialCursor.started', trialCursor.tStartRefresh)
        trials.addData('trialCursor.stopped', trialCursor.tStopRefresh)
        trials.addData('trialNum.started', trialNum.tStartRefresh)
        trials.addData('trialNum.stopped', trialNum.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed repRows repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'selectLoop'


# ------Prepare to start Routine "e"-------
continueRoutine = True
# update component parameters for each repeat
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
eComponents = [thanks, endResp]
for thisComponent in eComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
eClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "e"-------
while continueRoutine:
    # get current time
    t = eClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=eClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in eComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "e"-------
for thisComponent in eComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)
# the Routine "e" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
