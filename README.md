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
