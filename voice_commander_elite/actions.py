import sys
from typing import Type, Any

from voice_commander.actions import ActionBase

from .keybinds import find_bindings_file, read_bound_actions, KEYBINDS, Binding, binding_to_press_action

_found_bindings: dict[str, Binding] = {}

_all_actions: dict[str, Type[ActionBase]] = {}

try:
    _found_bindings.update(read_bound_actions(find_bindings_file()))
    for _bindname, _binding in _found_bindings.items():
        try:
            _action = binding_to_press_action(_binding)
        except Exception as exc:
            print(f'Error ignored: Failed to register binding for {_bindname}', exc, file=sys.stderr)
        name = f'{_bindname}Action'
        _all_actions[name] = _action
except Exception as e:
    print('Failed to read bindings!', e, file=sys.stderr)


# TODO: don't do this dynamically so users can take advantage of typing/intellisense. Maybe codegen all classes?
globals().update(_all_actions)
__all__ = list(_all_actions)

def __getattr__(name: str) -> Any:
    if name in _all_actions:
        return _all_actions[name]
    if not name.endswith('Action'):
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    bindname = name.removesuffix('Action')
    if bindname in KEYBINDS:
        raise RuntimeError(f'Did not find valid mouse button or keyboard key binding for {bindname!r} in your Elite Dangerous custom keybinds. Please make sure either the primary or secondary binding is set to a mouse button or keyboard key in your Elite Dangerous controls settings')
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
