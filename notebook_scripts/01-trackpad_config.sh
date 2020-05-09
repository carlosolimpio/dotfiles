#!/bin/bash

readonly ID=$(xinput list --id-only 'Synaptics s3203')
readonly TAPPING='libinput Tapping Enabled'
readonly NATURAL_SCROLLING='libinput Natural Scrolling Enabled'
readonly ENABLE=1
readonly DISABLE=0

# enables tapping
xinput --set-prop $ID "$TAPPING" $ENABLE

# enables natural scroll
xinput --set-prop $ID "$NATURAL_SCROLLING" $ENABLE
