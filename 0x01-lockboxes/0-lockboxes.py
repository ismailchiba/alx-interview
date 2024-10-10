#!/usr/bin/python3
"""
lockboxes:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Parameters:
        boxes (list of lists):
        A list where each index represents a box,
        and each box contains a list of keys (positive integers)
        that can unlock other boxes. The first box (boxes[0])
        is unlocked by default.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

    Method:
    - Start from the first box (index 0), which is already unlocked.
    - Collect keys from each unlocked box and attempt to unlock other boxes.
    - Use a set to track which boxes have been unlocked
        to avoid rechecking them.
    - If all boxes are unlocked by the end, return True.
        If there are still locked boxes, return False.
    """
    # Handle invalid input or empty input
    if not isinstance(boxes, list) or not boxes:
        return False
    # List to keep track of which boxes are unlocked
    unlockboxes = [False] * len(boxes)
    unlockboxes[0] = True

    # Keys we currently have (initially the keys in box 0)
    keys = boxes[0]

    # Iterate through the keys we collect
    for key in keys:
        if key >= len(boxes) or key < 0:
            continue
        # Ensure key is within valid range and unlock the corresponding box
        if key < len(boxes) and unlockboxes[key] is False:
            # Mark the box as unlocked
            unlockboxes[key] = True
            # Add the keys from the newly unlocked box to the list of keys
            keys.extend(boxes[key])

    # After attempting to unlock all boxes, check if all boxes are unlocked
    return unlockboxes.count(True) == len(boxes)
    # Another way to check is : using all() : return all(unlockboxes)
