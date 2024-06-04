# voice-commander-elite

Elite dangerous extension for the [voice-commander](https://github.com/spyoungtech/voice-commander) framework.

**Key features:**

- Provides predefined actions for all available Elite Dangerous keybinds
- Analyzes your local Elite Dangerous keybinds settings file to ensure actions are portable and always work, even if you change your keybinds

## Installation

```bash
pip install voice-commander-elite
```

## Usage

As Python code:
```python
from voice_commander.triggers import VoiceTrigger

from voice_commander_elite.actions import SupercruiseAction, LandingGearToggleAction
from voice_commander_elite.conditions import EliteDangerousIsActive
from voice_commander.profile import Profile

p = (Profile('elite-example')
    .add_trigger(
        VoiceTrigger("supercruise")
        .add_condition(EliteDangerousIsActive())
        .add_action(SupercruiseAction()))
    .add_trigger(
        VoiceTrigger('retract landing gear', 'lower landing gear')
        .add_condition(EliteDangerousIsActive())
        .add_action(LandingGearToggleAction())
))

p.run()
```

### Loading from serialized JSON

If saved to a profile JSON file, the above example produces substantially the following JSON:

```json
{
    "configuration": {
        "profile_name": "elite-example",
        "schema_version": "0",
        "triggers": [
            {
                "trigger_type": "voice_commander.triggers.VoiceTrigger",
                "actions": [
                    {
                        "action_type": "voice_commander_elite.actions.SupercruiseAction",
                        "action_config": {}
                    }
                ],
                "conditions": [
                    {
                        "condition_type": "voice_commander_elite.conditions.EliteDangerousIsActive",
                        "condition_config": {}
                    }
                ],
                "trigger_config": {
                    "*trigger_phrases": [
                        "supercruise"
                    ]
                }
            },
            {
                "trigger_type": "voice_commander.triggers.VoiceTrigger",
                "actions": [
                    {
                        "action_type": "voice_commander_elite.actions.LandingGearToggleAction",
                        "action_config": {}
                    }
                ],
                "conditions": [
                    {
                        "condition_type": "voice_commander_elite.conditions.EliteDangerousIsActive",
                        "condition_config": {}
                    }
                ],
                "trigger_config": {
                    "*trigger_phrases": [
                        "retract landing gear",
                        "lower landing gear"
                    ]
                }
            }
        ]
    }
}
```

To load and use this profile later in Python code, you can do the following:

```python
from voice_commander.profile import load_profile
# import the extension package before loading the profile!
# THIS IS IMPORTANT!
# The import triggers the reading of your keybind file and ensures that all actions/conditions are properly initialized.
import voice_commander_elite  # noqa

profile = load_profile('./elite-example.vcp.json')
profile.run()
```

### Serialization notes

When serialized to JSON, by default, the `action_type` will refer to the fully qualified names within this extension package. 
This _may_ cause the produced JSON to be incompatible with certain vanilla `voice-commander` features (since the specification for extensions is not yet defined).
Specifically: invoking profiles from the command line, since there's no mechanism built into `voice-commander` to ensure the extension module is imported, the `action_type` will not resolve 
properly. Though there are hacks to _make_ this work, until there is a formal extensions feature, we offer a better solution for this use case.
Because the actions and conditions in this package are just subclasses of regular `voice-commander` actions, you can choose to serialize using those standard `action_type`s as well 
by using the `.with_simplified_serialization` alternate constructor (or the `.wss` alias). This means that your profile will contain static bindings, so it won't be portable, but it 
will be compatible with vanilla `voice-commander` without the need to install or specify any extension (once generated, obviously).

TL;DR if you want to use the `voice-commander` CLI with profiles generated using `voice-commander-elite` actions, do the following:

```diff
-    .add_action(LandingGearToggleAction())
+    .add_action(LandingGearToggleAction.with_simplified_serialization()) # or .wss()
```

Again, remember that the generated profile will have static bindings and will not necessarily be portable or continue to work if you change your keybinds (you'll have to manually update your profile json).

If you apply this change to use `.wss()` to invoke all the actions/conditions, the following JSON file will be produced:

```json
{
    "configuration": {
        "profile_name": "elite-example",
        "schema_version": "0",
        "triggers": [
            {
                "trigger_type": "voice_commander.triggers.VoiceTrigger",
                "actions": [
                    {
                        "action_type": "voice_commander.actions.AHKPressAction",
                        "conditions": [],
                        "action_config": {
                            "key": "s"
                        }
                    }
                ],
                "conditions": [
                    {
                        "condition_type": "voice_commander.conditions.AHKWindowIsActive",
                        "condition_config": {
                            "title": "Elite - Dangerous (CLIENT)"
                        }
                    }
                ],
                "trigger_config": {
                    "*trigger_phrases": [
                        "supercruise"
                    ]
                }
            },
            {
                "trigger_type": "voice_commander.triggers.VoiceTrigger",
                "actions": [
                    {
                        "action_type": "voice_commander.actions.AHKPressAction",
                        "conditions": [],
                        "action_config": {
                            "key": "l"
                        }
                    }
                ],
                "conditions": [
                    {
                        "condition_type": "voice_commander.conditions.AHKWindowIsActive",
                        "condition_config": {
                            "title": "Elite - Dangerous (CLIENT)"
                        }
                    }
                ],
                "trigger_config": {
                    "*trigger_phrases": [
                        "retract landing gear",
                        "lower landing gear"
                    ]
                }
            }
        ]
    }
}
```

As you can notice the resulting JSON has **no references to the extension package!** - it also has static keybindings present in the JSON (which were previously pulled from my personal elite dangerous bindings).

Hopefully, this will not be necessary in the not-too-far future and eventually this constructor will be obsoleted.

## List of known possible actions

As of 4.1, these are the known keybinds. You will only be able to import these names if you have a proper mouse button or keyboard key assigned to the keybind. This may not be possible for some of these actions. So-called 'buggy' keybinds are omitted from this list.

If new keybinds are added to the game in a future version that are (obviously) not known at time of writing, they will still be detected and usable dynamically.

- `BackwardKeyAction`
- `BackwardThrustButtonAction`
- `BackwardThrustButton_LandingAction`
- `BlockMouseDecayAction`
- `CamPitchDownAction`
- `CamPitchUpAction`
- `CamTranslateBackwardAction`
- `CamTranslateDownAction`
- `CamTranslateForwardAction`
- `CamTranslateLeftAction`
- `CamTranslateRightAction`
- `CamTranslateUpAction`
- `CamTranslateZHoldAction`
- `CamYawLeftAction`
- `CamYawRightAction`
- `CamZoomInAction`
- `CamZoomOutAction`
- `ChargeECMAction`
- `CommanderCreator_RedoAction`
- `CommanderCreator_Rotation_MouseToggleAction`
- `CommanderCreator_UndoAction`
- `CycleFireGroupNextAction`
- `CycleFireGroupPreviousAction`
- `CycleNextHostileTargetAction`
- `CycleNextPageAction`
- `CycleNextPanelAction`
- `CycleNextSubsystemAction`
- `CycleNextTargetAction`
- `CyclePreviousHostileTargetAction`
- `CyclePreviousPageAction`
- `CyclePreviousPanelAction`
- `CyclePreviousSubsystemAction`
- `CyclePreviousTargetAction`
- `DecreaseSpeedButtonMaxAction`
- `DeployHardpointToggleAction`
- `DeployHeatSinkAction`
- `DisableRotationCorrectToggleAction`
- `DownThrustButtonAction`
- `DownThrustButton_LandingAction`
- `EjectAllCargoAction`
- `EngineColourToggleAction`
- `ExplorationFSSCameraPitchDecreaseButtonAction`
- `ExplorationFSSCameraPitchIncreaseButtonAction`
- `ExplorationFSSCameraYawDecreaseButtonAction`
- `ExplorationFSSCameraYawIncreaseButtonAction`
- `ExplorationFSSDiscoveryScanAction`
- `ExplorationFSSEnterAction`
- `ExplorationFSSMiniZoomInAction`
- `ExplorationFSSMiniZoomOutAction`
- `ExplorationFSSQuitAction`
- `ExplorationFSSRadioTuningX_DecreaseAction`
- `ExplorationFSSRadioTuningX_IncreaseAction`
- `ExplorationFSSShowHelpAction`
- `ExplorationFSSTargetAction`
- `ExplorationFSSZoomInAction`
- `ExplorationFSSZoomOutAction`
- `ExplorationSAAChangeScannedAreaViewToggleAction`
- `ExplorationSAAExitThirdPersonAction`
- `ExplorationSAANextGenusAction`
- `ExplorationSAAPreviousGenusAction`
- `FStopDecAction`
- `FStopIncAction`
- `FireChaffLauncherAction`
- `FixCameraRelativeToggleAction`
- `FixCameraWorldToggleAction`
- `FocusCommsPanelAction`
- `FocusCommsPanel_HumanoidAction`
- `FocusLeftPanelAction`
- `FocusRadarPanelAction`
- `FocusRightPanelAction`
- `ForwardKeyAction`
- `ForwardThrustButtonAction`
- `ForwardThrustButton_LandingAction`
- `FreeCamSpeedDecAction`
- `FreeCamSpeedIncAction`
- `FreeCamToggleHUDAction`
- `FreeCamZoomInAction`
- `FreeCamZoomOutAction`
- `FriendsMenuAction`
- `GalaxyMapHomeAction`
- `GalaxyMapOpenAction`
- `GalaxyMapOpen_HumanoidAction`
- `GalnetAudio_ClearQueueAction`
- `GalnetAudio_Play_PauseAction`
- `GalnetAudio_SkipBackwardAction`
- `GalnetAudio_SkipForwardAction`
- `HMDResetAction`
- `HeadLookPitchDownAction`
- `HeadLookPitchUpAction`
- `HeadLookResetAction`
- `HeadLookToggleAction`
- `HeadLookYawLeftAction`
- `HeadLookYawRightAction`
- `HumanoidBackwardButtonAction`
- `HumanoidBatteryAction`
- `HumanoidClearAuthorityLevelAction`
- `HumanoidConflictContextualUIButtonAction`
- `HumanoidCrouchButtonAction`
- `HumanoidEmoteSlot1Action`
- `HumanoidEmoteSlot2Action`
- `HumanoidEmoteSlot3Action`
- `HumanoidEmoteSlot4Action`
- `HumanoidEmoteSlot5Action`
- `HumanoidEmoteSlot6Action`
- `HumanoidEmoteSlot7Action`
- `HumanoidEmoteSlot8Action`
- `HumanoidEmoteWheelButtonAction`
- `HumanoidForwardButtonAction`
- `HumanoidHealthPackAction`
- `HumanoidHideWeaponButtonAction`
- `HumanoidItemWheelButtonAction`
- `HumanoidItemWheelButton_XLeftAction`
- `HumanoidItemWheelButton_XRightAction`
- `HumanoidItemWheelButton_YDownAction`
- `HumanoidItemWheelButton_YUpAction`
- `HumanoidJumpButtonAction`
- `HumanoidMeleeButtonAction`
- `HumanoidOpenAccessPanelButtonAction`
- `HumanoidPingAction`
- `HumanoidPitchDownButtonAction`
- `HumanoidPitchUpButtonAction`
- `HumanoidPrimaryFireButtonAction`
- `HumanoidPrimaryInteractButtonAction`
- `HumanoidReloadButtonAction`
- `HumanoidRotateLeftButtonAction`
- `HumanoidRotateRightButtonAction`
- `HumanoidSecondaryInteractButtonAction`
- `HumanoidSelectEMPGrenadeAction`
- `HumanoidSelectFragGrenadeAction`
- `HumanoidSelectNextGrenadeTypeButtonAction`
- `HumanoidSelectNextWeaponButtonAction`
- `HumanoidSelectPreviousGrenadeTypeButtonAction`
- `HumanoidSelectPreviousWeaponButtonAction`
- `HumanoidSelectPrimaryWeaponButtonAction`
- `HumanoidSelectSecondaryWeaponButtonAction`
- `HumanoidSelectShieldGrenadeAction`
- `HumanoidSelectUtilityWeaponButtonAction`
- `HumanoidSprintButtonAction`
- `HumanoidStrafeLeftButtonAction`
- `HumanoidStrafeRightButtonAction`
- `HumanoidSwitchToCompAnalyserAction`
- `HumanoidSwitchToRechargeToolAction`
- `HumanoidSwitchToSuitToolAction`
- `HumanoidSwitchWeaponAction`
- `HumanoidThrowGrenadeButtonAction`
- `HumanoidToggleFlashlightButtonAction`
- `HumanoidToggleMissionHelpPanelButtonAction`
- `HumanoidToggleNightVisionButtonAction`
- `HumanoidToggleShieldsButtonAction`
- `HumanoidToggleToolModeButtonAction`
- `HumanoidUtilityWheelCycleModeAction`
- `HumanoidWalkButtonAction`
- `HumanoidZoomButtonAction`
- `HyperSuperCombinationAction`
- `HyperspaceAction`
- `IncreaseEnginesPowerAction`
- `IncreaseSpeedButtonMaxAction`
- `IncreaseSystemsPowerAction`
- `IncreaseWeaponsPowerAction`
- `LandingGearToggleAction`
- `LeftThrustButtonAction`
- `LeftThrustButton_LandingAction`
- `MicrophoneMuteAction`
- `MouseResetAction`
- `MoveFreeCamBackwardsAction`
- `MoveFreeCamDownAction`
- `MoveFreeCamForwardAction`
- `MoveFreeCamLeftAction`
- `MoveFreeCamRightAction`
- `MoveFreeCamUpAction`
- `MultiCrewCockpitUICycleBackwardAction`
- `MultiCrewCockpitUICycleForwardAction`
- `MultiCrewPrimaryFireAction`
- `MultiCrewPrimaryUtilityFireAction`
- `MultiCrewSecondaryFireAction`
- `MultiCrewSecondaryUtilityFireAction`
- `MultiCrewThirdPersonFovInButtonAction`
- `MultiCrewThirdPersonFovOutButtonAction`
- `MultiCrewThirdPersonPitchDownButtonAction`
- `MultiCrewThirdPersonPitchUpButtonAction`
- `MultiCrewThirdPersonYawLeftButtonAction`
- `MultiCrewThirdPersonYawRightButtonAction`
- `MultiCrewToggleModeAction`
- `NightVisionToggleAction`
- `OpenCodexGoToDiscoveryAction`
- `OpenOrdersAction`
- `OrbitLinesToggleAction`
- `OrderAggressiveBehaviourAction`
- `OrderDefensiveBehaviourAction`
- `OrderFocusTargetAction`
- `OrderFollowAction`
- `OrderHoldFireAction`
- `OrderHoldPositionAction`
- `OrderRequestDockAction`
- `PauseAction`
- `PhotoCameraToggleAction`
- `PhotoCameraToggle_HumanoidAction`
- `PitchCameraDownAction`
- `PitchCameraUpAction`
- `PitchDownButtonAction`
- `PitchDownButton_LandingAction`
- `PitchUpButtonAction`
- `PitchUpButton_LandingAction`
- `PlayerHUDModeToggleAction`
- `PrimaryFireAction`
- `QuickCommsPanelAction`
- `QuickCommsPanel_HumanoidAction`
- `QuitCameraAction`
- `RadarDecreaseRangeAction`
- `RadarIncreaseRangeAction`
- `RecallDismissShipAction`
- `ResetPowerDistributionAction`
- `RightThrustButtonAction`
- `RightThrustButton_LandingAction`
- `RollCameraLeftAction`
- `RollCameraRightAction`
- `RollLeftButtonAction`
- `RollLeftButton_LandingAction`
- `RollRightButtonAction`
- `RollRightButton_LandingAction`
- `SAAThirdPersonFovInButtonAction`
- `SAAThirdPersonFovOutButtonAction`
- `SAAThirdPersonPitchDownButtonAction`
- `SAAThirdPersonPitchUpButtonAction`
- `SAAThirdPersonYawLeftButtonAction`
- `SAAThirdPersonYawRightButtonAction`
- `SecondaryFireAction`
- `SelectHighestThreatAction`
- `SelectTargetAction`
- `SelectTargetsTargetAction`
- `SetSpeed100Action`
- `SetSpeed25Action`
- `SetSpeed50Action`
- `SetSpeed75Action`
- `SetSpeedMinus100Action`
- `SetSpeedMinus25Action`
- `SetSpeedMinus50Action`
- `SetSpeedMinus75Action`
- `SetSpeedZeroAction`
- `ShipSpotLightToggleAction`
- `ShowPGScoreSummaryInputAction`
- `SteerLeftButtonAction`
- `SteerRightButtonAction`
- `StoreCamZoomInAction`
- `StoreCamZoomOutAction`
- `StoreEnableRotationAction`
- `StoreToggleAction`
- `SupercruiseAction`
- `SystemMapOpenAction`
- `SystemMapOpen_HumanoidAction`
- `TargetNextRouteSystemAction`
- `TargetWingman0Action`
- `TargetWingman1Action`
- `TargetWingman2Action`
- `ToggleAdvanceModeAction`
- `ToggleButtonUpInputAction`
- `ToggleCargoScoopAction`
- `ToggleDriveAssistAction`
- `ToggleFlightAssistAction`
- `ToggleFreeCamAction`
- `ToggleReverseThrottleInputAction`
- `ToggleReverseThrottleInputFreeCamAction`
- `ToggleRotationLockAction`
- `TriggerFieldNeutraliserAction`
- `UIFocusAction`
- `UI_BackAction`
- `UI_DownAction`
- `UI_LeftAction`
- `UI_RightAction`
- `UI_SelectAction`
- `UI_ToggleAction`
- `UI_UpAction`
- `UpThrustButtonAction`
- `UpThrustButton_LandingAction`
- `UseAlternateFlightValuesToggleAction`
- `UseBoostJuiceAction`
- `UseShieldCellAction`
- `VanityCameraEightAction`
- `VanityCameraFiveAction`
- `VanityCameraFourAction`
- `VanityCameraNineAction`
- `VanityCameraOneAction`
- `VanityCameraScrollLeftAction`
- `VanityCameraScrollRightAction`
- `VanityCameraSevenAction`
- `VanityCameraSixAction`
- `VanityCameraTenAction`
- `VanityCameraThreeAction`
- `VanityCameraTwoAction`
- `VerticalThrustersButtonAction`
- `WeaponColourToggleAction`
- `WingNavLockAction`
- `YawCameraLeftAction`
- `YawCameraRightAction`
- `YawLeftButtonAction`
- `YawLeftButton_LandingAction`
- `YawRightButtonAction`
- `YawRightButton_LandingAction`
- `YawToRollButtonAction`
