from __future__ import annotations

import enum
import os.path
import warnings
from pathlib import Path
from typing import Literal, TypeAlias, Type
from bs4 import BeautifulSoup, Tag
from voice_commander.actions import AHKPressAction
import re


def _binding_tag(tag: Tag):
    return tag.find('Primary')


def _bindings_with_mouse_or_keyboard(tag: Tag):
    primary = tag.find('Primary')
    secondary = tag.find('Secondary')
    if not primary and not secondary:
        return False
    if primary.get('Device', '') in ('Keyboard', 'Mouse'):
        return True
    if secondary.get('Device', '') in ('Keyboard', 'Mouse'):
        return True
    return False


class BindingDevice(enum.IntEnum):
    KEYBOARD = 0
    MOUSE = 1


AHK_KEY_MAPPING = {
    BindingDevice.KEYBOARD: {
        "Key_Escape": "Escape",
        "Key_1": "1",
        "Key_2": "2",
        "Key_3": "3",
        "Key_4": "4",
        "Key_5": "5",
        "Key_6": "6",
        "Key_7": "7",
        "Key_8": "8",
        "Key_9": "9",
        "Key_0": "0",
        "Key_Minus": "-",
        "Key_Equals": "=",
        "Key_Backspace": "Backspace",
        "Key_Tab": "Tab",
        "Key_Q": "q",
        "Key_W": "w",
        "Key_E": "e",
        "Key_R": "r",
        "Key_T": "t",
        "Key_Y": "y",
        "Key_U": "u",
        "Key_I": "i",
        "Key_O": "o",
        "Key_P": "p",
        "Key_LeftBracket": "[",
        "Key_RightBracket": "]",
        "Key_Enter": "",
        "Key_LeftControl": "",
        "Key_A": "a",
        "Key_S": "s",
        "Key_D": "d",
        "Key_F": "f",
        "Key_G": "g",
        "Key_H": "h",
        "Key_J": "j",
        "Key_K": "k",
        "Key_L": "l",
        "Key_SemiColon": ";",
        "Key_Apostrophe": "'",
        "Key_Grave": "``",
        "Key_LeftShift": "LShift",
        "Key_BackSlash": "\\",
        "Key_Z": "z",
        "Key_X": "x",
        "Key_C": "c",
        "Key_V": "v",
        "Key_B": "b",
        "Key_N": "n",
        "Key_M": "m",
        "Key_Comma": ",",
        "Key_Period": ".",
        "Key_Slash": "/",
        "Key_RightShift": "RShift",
        "Key_Numpad_Multiply": "NumpadMult",
        "Key_LeftAlt": "LAlt",
        "Key_Space": "Space",
        "Key_CapsLock": "CapsLock",
        "Key_F1": "F1",
        "Key_F2": "F2",
        "Key_F3": "F3",
        "Key_F4": "F4",
        "Key_F5": "F5",
        "Key_F6": "F6",
        "Key_F7": "F7",
        "Key_F8": "F8",
        "Key_F9": "F9",
        "Key_F10": "F10",
        "Key_NumLock": "NumLock",
        "Key_ScrollLock": "ScrollLock",
        "Key_Numpad_7": "Numpad7",
        "Key_Numpad_8": "Numpad8",
        "Key_Numpad_9": "Numpad9",
        "Key_Numpad_Subtract": "NumpadSub",
        "Key_Numpad_4": "Numpad4",
        "Key_Numpad_5": "Numpad5",
        "Key_Numpad_6": "Numpad6",
        "Key_Numpad_Add": "NumpadAdd",
        "Key_Numpad_1": "Numpad1",
        "Key_Numpad_2": "Numpad2",
        "Key_Numpad_3": "Numpad3",
        "Key_Numpad_0": "Numpad0",
        "Key_Numpad_Decimal": "NumpadDot",
        "Key_OEM_102": None,
        "Key_F11": "F11",
        "Key_F12": "F12",
        "Key_F13": "F13",
        "Key_F14": "F14",
        "Key_F15": "F15",
        "Key_Kana": None,
        "Key_ABNT_C1": None,
        "Key_Convert": None,
        "Key_NoConvert": None,
        "Key_Yen": None,
        "Key_ABNT_C2": None,
        "Key_Numpad_Equals": None,
        "Key_PrevTrack": "Media_Prev",
        "Key_AT": None,
        "Key_Colon": None,
        "Key_Underline": None,
        "Key_Kanji": None,
        "Key_Stop": "Media_Stop",  # This may be wrong
        "Key_AX": None,
        "Key_Unlabeled": None,
        "Key_NextTrack": "Media_Next",
        "Key_Numpad_Enter": "NumpadEnter",
        "Key_RightControl": "RCtrl",
        "Key_Mute": "Volume_Mute",
        "Key_Calculator": "Launch_App2",
        "Key_PlayPause": "Media_Play_Pause",
        "Key_MediaStop": "Media_Stop",
        "Key_VolumeDown": "Volume_Down",
        "Key_VolumeUp": "Volume_Up",
        "Key_WebHome": "Browser_Home",
        "Key_Numpad_Comma": None,
        "Key_Numpad_Divide": "NumpadDiv",
        "Key_SYSRQ": None,
        "Key_RightAlt": "RAlt",
        "Key_Pause": "Pause",
        "Key_Home": "Home",
        "Key_UpArrow": "Up",
        "Key_PageUp": "PgUp",
        "Key_LeftArrow": "Left",
        "Key_RightArrow": "Right",
        "Key_End": "End",
        "Key_DownArrow": "Down",
        "Key_PageDown": "PgDn",
        "Key_Insert": "Ins",
        "Key_Delete": "Del",
        "Key_LeftWin": "LWin",
        "Key_RightWin": "RWin",
        "Key_Apps": "AppsKey",
        "Key_Power": None,
        "Key_Sleep": "Sleep",
        "Key_Wake": None,
        "Key_WebSearch": "Browser_Search",
        "Key_WebFavourites": "Browser_Favorites",
        "Key_WebRefresh": "Browser_Refresh",
        "Key_WebStop": "Browser_Stop",
        "Key_WebForward": "Browser_Forward",
        "Key_WebBack": "Browser_Back",
        "Key_MyComputer": "Launch_App1",
        "Key_Mail": "Launch_Mail",
        "Key_MediaSelect": "Launch_Media",  # I think?
        "Key_GreenModifier": None,
        "Key_OrangeModifier": None,
    },
    BindingDevice.MOUSE: {
        "Mouse_1": "LButton",
        "Mouse_2": "RButton",
        "Mouse_3": "MButton",
        "Mouse_4": "XButton1",
    },
}


class Binding:
    def __init__(self, name: str, device: BindingDevice, key: str):
        self.name: str = name
        self.device: BindingDevice = device
        self.key: str = key

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name!r}, device={self.device!r}, key={self.key!r})'

def binding_to_press_action(binding: Binding) -> Type[AHKPressAction]:
    device_map = AHK_KEY_MAPPING[binding.device]
    ahk_key = device_map[binding.key]
    assert ahk_key is not None
    class InitMixin:
        def __init__(self, *, key=None, **kwargs):
            if key is not None:
                warnings.warn('parameter key was provided, but will be ignored', UserWarning, stacklevel=2)

            super().__init__(key=ahk_key, **kwargs)
        @classmethod
        def fqn(cls) -> str:
            return f'voice_commander_elite.actions.{binding.name}Action'
    klass = type(f'{binding.name}Action', (InitMixin, AHKPressAction), {})
    return klass

def _extract_binding(tag: Tag) -> tuple[BindingDevice, str]:
    tag_device = tag.get('Device', '')
    key = tag.get('Key', None)
    assert key is not None
    match tag_device:
        case "Keyboard":
            device = BindingDevice.KEYBOARD
        case "Mouse":
            device = BindingDevice.MOUSE
        case _:
            raise ValueError(f'invalid tag')
    return device, key

def extract_binding(tag: Tag) -> Binding:
    name = tag.name
    try:
        inner_tag = tag.find('Primary')
        assert inner_tag is not None
        device, key = _extract_binding(inner_tag)
    except (AssertionError, ValueError):
        try:
            inner_tag = tag.find('Secondary')
            assert inner_tag is not None
            device, key = _extract_binding(inner_tag)
        except (AssertionError, ValueError) as exc:
            raise ValueError(f'invalid tag') from exc
    return Binding(name=name, device=device, key=key)

APPDATA_BINDING_OPTIONS_DIR = os.path.expanduser('~/AppData/Local/Frontier Developments/Elite Dangerous/Options/Bindings')

def _to_version_tuple(s: str) -> tuple[int, ...]:
    return tuple([int(part) for part in s.split('.')])


def find_bindings_file() -> Path:
    if 'VOICE_COMMANDER_ELITE_BINDINGS_FILE' in os.environ:
        return Path(os.environ['VOICE_COMMANDER_ELITE_BINDINGS_FILE'])
    available_files = os.listdir(APPDATA_BINDING_OPTIONS_DIR)
    pattern = re.compile(r'^Custom\.(\d+(?:\.\d+)+)\.binds$')
    highest = None
    for filename in available_files:
        match = re.match(pattern, filename)
        if match:
            version = _to_version_tuple(match.group(1))
            if highest is None:
                highest = (filename, version)
            else:
                highest_version = highest[1]
                if version > highest_version:
                    highest = (filename, version)
    if highest is None:
        raise ValueError(f'could not find binding file in {APPDATA_BINDING_OPTIONS_DIR!r}. Please set the VOICE_COMMANDER_ELITE_BINDINGS_FILE environment variable to specify your custom bindings file')
    fp = os.path.join(APPDATA_BINDING_OPTIONS_DIR, highest[0])
    return Path(fp)




def read_bound_actions(bindings_file: str | Path) -> dict[str, Binding]:
    fp = Path(bindings_file).absolute()
    with open(fp) as f:
        text = f.read()
    soup = BeautifulSoup(text, features='xml')
    root = soup.find('Root')
    bindings = {}
    for binding_tag in root.find_all(_bindings_with_mouse_or_keyboard):
        binding = extract_binding(binding_tag)
        bindings[binding_tag.name] = binding
    return bindings




KEYBINDS = [
    'MouseReset',
    'BlockMouseDecay',
    'YawLeftButton',
    'YawRightButton',
    'YawToRollButton',
    'RollLeftButton',
    'RollRightButton',
    'PitchUpButton',
    'PitchDownButton',
    'LeftThrustButton',
    'RightThrustButton',
    'UpThrustButton',
    'DownThrustButton',
    'ForwardThrustButton',
    'BackwardThrustButton',
    'UseAlternateFlightValuesToggle',
    'ToggleReverseThrottleInput',
    'ForwardKey',
    'BackwardKey',
    'SetSpeedMinus100',
    'SetSpeedMinus75',
    'SetSpeedMinus50',
    'SetSpeedMinus25',
    'SetSpeedZero',
    'SetSpeed25',
    'SetSpeed50',
    'SetSpeed75',
    'SetSpeed100',
    'YawLeftButton_Landing',
    'YawRightButton_Landing',
    'PitchUpButton_Landing',
    'PitchDownButton_Landing',
    'RollLeftButton_Landing',
    'RollRightButton_Landing',
    'LeftThrustButton_Landing',
    'RightThrustButton_Landing',
    'UpThrustButton_Landing',
    'DownThrustButton_Landing',
    'ForwardThrustButton_Landing',
    'BackwardThrustButton_Landing',
    'ToggleFlightAssist',
    'UseBoostJuice',
    'HyperSuperCombination',
    'Supercruise',
    'Hyperspace',
    'DisableRotationCorrectToggle',
    'OrbitLinesToggle',
    'SelectTarget',
    'CycleNextTarget',
    'CyclePreviousTarget',
    'SelectHighestThreat',
    'CycleNextHostileTarget',
    'CyclePreviousHostileTarget',
    'TargetWingman0',
    'TargetWingman1',
    'TargetWingman2',
    'SelectTargetsTarget',
    'WingNavLock',
    'CycleNextSubsystem',
    'CyclePreviousSubsystem',
    'TargetNextRouteSystem',
    'PrimaryFire',
    'SecondaryFire',
    'CycleFireGroupNext',
    'CycleFireGroupPrevious',
    'DeployHardpointToggle',
    'ToggleButtonUpInput',
    'DeployHeatSink',
    'ShipSpotLightToggle',
    'RadarIncreaseRange',
    'RadarDecreaseRange',
    'IncreaseEnginesPower',
    'IncreaseWeaponsPower',
    'IncreaseSystemsPower',
    'ResetPowerDistribution',
    'HMDReset',
    'ToggleCargoScoop',
    'EjectAllCargo',
    'LandingGearToggle',
    'MicrophoneMute',
    'UseShieldCell',
    'FireChaffLauncher',
    'TriggerFieldNeutraliser',
    'ChargeECM',
    'WeaponColourToggle',
    'EngineColourToggle',
    'NightVisionToggle',
    'UIFocus',
    'FocusLeftPanel',
    'FocusCommsPanel',
    'QuickCommsPanel',
    'FocusRadarPanel',
    'FocusRightPanel',
    'GalaxyMapOpen',
    'SystemMapOpen',
    'ShowPGScoreSummaryInput',
    'HeadLookToggle',
    'Pause',
    'FriendsMenu',
    'OpenCodexGoToDiscovery',
    'PlayerHUDModeToggle',
    'ExplorationFSSEnter',
    'UI_Up',
    'UI_Down',
    'UI_Left',
    'UI_Right',
    'UI_Select',
    'UI_Back',
    'UI_Toggle',
    'CycleNextPanel',
    'CyclePreviousPanel',
    'CycleNextPage',
    'CyclePreviousPage',
    'HeadLookReset',
    'HeadLookPitchUp',
    'HeadLookPitchDown',
    'HeadLookYawLeft',
    'HeadLookYawRight',
    'CamPitchUp',
    'CamPitchDown',
    'CamYawLeft',
    'CamYawRight',
    'CamTranslateForward',
    'CamTranslateBackward',
    'CamTranslateLeft',
    'CamTranslateRight',
    'CamTranslateUp',
    'CamTranslateDown',
    'CamZoomIn',
    'CamZoomOut',
    'CamTranslateZHold',
    'GalaxyMapHome',
    'ToggleDriveAssist',
    'SteerLeftButton',
    'SteerRightButton',
    'BuggyRollLeftButton',
    'BuggyRollRightButton',
    'BuggyPitchUpButton',
    'BuggyPitchDownButton',
    'VerticalThrustersButton',
    'BuggyPrimaryFireButton',
    'BuggySecondaryFireButton',
    'AutoBreakBuggyButton',
    'HeadlightsBuggyButton',
    'ToggleBuggyTurretButton',
    'BuggyCycleFireGroupNext',
    'BuggyCycleFireGroupPrevious',
    'SelectTarget_Buggy',
    'BuggyTurretYawLeftButton',
    'BuggyTurretYawRightButton',
    'BuggyTurretPitchUpButton',
    'BuggyTurretPitchDownButton',
    'BuggyToggleReverseThrottleInput',
    'IncreaseSpeedButtonMax',
    'DecreaseSpeedButtonMax',
    'IncreaseEnginesPower_Buggy',
    'IncreaseWeaponsPower_Buggy',
    'IncreaseSystemsPower_Buggy',
    'ResetPowerDistribution_Buggy',
    'ToggleCargoScoop_Buggy',
    'EjectAllCargo_Buggy',
    'RecallDismissShip',
    'UIFocus_Buggy',
    'FocusLeftPanel_Buggy',
    'FocusCommsPanel_Buggy',
    'QuickCommsPanel_Buggy',
    'FocusRadarPanel_Buggy',
    'FocusRightPanel_Buggy',
    'GalaxyMapOpen_Buggy',
    'SystemMapOpen_Buggy',
    'OpenCodexGoToDiscovery_Buggy',
    'PlayerHUDModeToggle_Buggy',
    'HeadLookToggle_Buggy',
    'MultiCrewToggleMode',
    'MultiCrewPrimaryFire',
    'MultiCrewSecondaryFire',
    'MultiCrewPrimaryUtilityFire',
    'MultiCrewSecondaryUtilityFire',
    'MultiCrewThirdPersonYawLeftButton',
    'MultiCrewThirdPersonYawRightButton',
    'MultiCrewThirdPersonPitchUpButton',
    'MultiCrewThirdPersonPitchDownButton',
    'MultiCrewThirdPersonFovOutButton',
    'MultiCrewThirdPersonFovInButton',
    'MultiCrewCockpitUICycleForward',
    'MultiCrewCockpitUICycleBackward',
    'OrderRequestDock',
    'OrderDefensiveBehaviour',
    'OrderAggressiveBehaviour',
    'OrderFocusTarget',
    'OrderHoldFire',
    'OrderHoldPosition',
    'OrderFollow',
    'OpenOrders',
    'PhotoCameraToggle',
    'PhotoCameraToggle_Buggy',
    'PhotoCameraToggle_Humanoid',
    'VanityCameraScrollLeft',
    'VanityCameraScrollRight',
    'ToggleFreeCam',
    'VanityCameraOne',
    'VanityCameraTwo',
    'VanityCameraThree',
    'VanityCameraFour',
    'VanityCameraFive',
    'VanityCameraSix',
    'VanityCameraSeven',
    'VanityCameraEight',
    'VanityCameraNine',
    'VanityCameraTen',
    'FreeCamToggleHUD',
    'FreeCamSpeedInc',
    'FreeCamSpeedDec',
    'ToggleReverseThrottleInputFreeCam',
    'MoveFreeCamForward',
    'MoveFreeCamBackwards',
    'MoveFreeCamRight',
    'MoveFreeCamLeft',
    'MoveFreeCamUp',
    'MoveFreeCamDown',
    'PitchCameraUp',
    'PitchCameraDown',
    'YawCameraLeft',
    'YawCameraRight',
    'RollCameraLeft',
    'RollCameraRight',
    'ToggleRotationLock',
    'FixCameraRelativeToggle',
    'FixCameraWorldToggle',
    'QuitCamera',
    'ToggleAdvanceMode',
    'FreeCamZoomIn',
    'FreeCamZoomOut',
    'FStopDec',
    'FStopInc',
    'CommanderCreator_Undo',
    'CommanderCreator_Redo',
    'CommanderCreator_Rotation_MouseToggle',
    'GalnetAudio_Play_Pause',
    'GalnetAudio_SkipForward',
    'GalnetAudio_SkipBackward',
    'GalnetAudio_ClearQueue',
    'ExplorationFSSCameraPitchIncreaseButton',
    'ExplorationFSSCameraPitchDecreaseButton',
    'ExplorationFSSCameraYawIncreaseButton',
    'ExplorationFSSCameraYawDecreaseButton',
    'ExplorationFSSZoomIn',
    'ExplorationFSSZoomOut',
    'ExplorationFSSMiniZoomIn',
    'ExplorationFSSMiniZoomOut',
    'ExplorationFSSRadioTuningX_Increase',
    'ExplorationFSSRadioTuningX_Decrease',
    'ExplorationFSSDiscoveryScan',
    'ExplorationFSSQuit',
    'ExplorationFSSTarget',
    'ExplorationFSSShowHelp',
    'ExplorationSAAChangeScannedAreaViewToggle',
    'ExplorationSAAExitThirdPerson',
    'ExplorationSAANextGenus',
    'ExplorationSAAPreviousGenus',
    'SAAThirdPersonYawLeftButton',
    'SAAThirdPersonYawRightButton',
    'SAAThirdPersonPitchUpButton',
    'SAAThirdPersonPitchDownButton',
    'SAAThirdPersonFovOutButton',
    'SAAThirdPersonFovInButton',
    'HumanoidForwardButton',
    'HumanoidBackwardButton',
    'HumanoidStrafeLeftButton',
    'HumanoidStrafeRightButton',
    'HumanoidRotateLeftButton',
    'HumanoidRotateRightButton',
    'HumanoidPitchUpButton',
    'HumanoidPitchDownButton',
    'HumanoidSprintButton',
    'HumanoidWalkButton',
    'HumanoidCrouchButton',
    'HumanoidJumpButton',
    'HumanoidPrimaryInteractButton',
    'HumanoidSecondaryInteractButton',
    'HumanoidItemWheelButton',
    'HumanoidEmoteWheelButton',
    'HumanoidUtilityWheelCycleMode',
    'HumanoidItemWheelButton_XLeft',
    'HumanoidItemWheelButton_XRight',
    'HumanoidItemWheelButton_YUp',
    'HumanoidItemWheelButton_YDown',
    'HumanoidPrimaryFireButton',
    'HumanoidZoomButton',
    'HumanoidThrowGrenadeButton',
    'HumanoidMeleeButton',
    'HumanoidReloadButton',
    'HumanoidSwitchWeapon',
    'HumanoidSelectPrimaryWeaponButton',
    'HumanoidSelectSecondaryWeaponButton',
    'HumanoidSelectUtilityWeaponButton',
    'HumanoidSelectNextWeaponButton',
    'HumanoidSelectPreviousWeaponButton',
    'HumanoidHideWeaponButton',
    'HumanoidSelectNextGrenadeTypeButton',
    'HumanoidSelectPreviousGrenadeTypeButton',
    'HumanoidToggleFlashlightButton',
    'HumanoidToggleNightVisionButton',
    'HumanoidToggleShieldsButton',
    'HumanoidClearAuthorityLevel',
    'HumanoidHealthPack',
    'HumanoidBattery',
    'HumanoidSelectFragGrenade',
    'HumanoidSelectEMPGrenade',
    'HumanoidSelectShieldGrenade',
    'HumanoidSwitchToRechargeTool',
    'HumanoidSwitchToCompAnalyser',
    'HumanoidSwitchToSuitTool',
    'HumanoidToggleToolModeButton',
    'HumanoidToggleMissionHelpPanelButton',
    'HumanoidPing',
    'GalaxyMapOpen_Humanoid',
    'SystemMapOpen_Humanoid',
    'FocusCommsPanel_Humanoid',
    'QuickCommsPanel_Humanoid',
    'HumanoidOpenAccessPanelButton',
    'HumanoidConflictContextualUIButton',
    'StoreEnableRotation',
    'StoreCamZoomIn',
    'StoreCamZoomOut',
    'StoreToggle',
    'HumanoidEmoteSlot1',
    'HumanoidEmoteSlot2',
    'HumanoidEmoteSlot3',
    'HumanoidEmoteSlot4',
    'HumanoidEmoteSlot5',
    'HumanoidEmoteSlot6',
    'HumanoidEmoteSlot7',
    'HumanoidEmoteSlot8',
]
