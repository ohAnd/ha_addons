**Version 0.0.8-fix3** published on 08.11.2026
- Maintenance release, no functional changes
- Rebuilt on Home Assistant's current build toolchain; the retired builder it used before
  has been announced for removal, which would have stopped add-on builds without notice
- ACTION REQUIRED for 32-bit installations: armhf, armv7 and i386 no longer receive
  updates. The new toolchain builds natively and GitHub offers no 32-bit runners. Existing
  installations keep running on 0.0.8-fix2; Home Assistant deprecated 32-bit installation
  methods in 2025.6, so moving to a 64-bit OS is the path forward

**Version 0.0.8-fix2** published on 01.01.2026
- adapt to current TRMNL fw
- Enhance image footer functionality by using absolute paths for fonts and adding compatibility flag
- adapt dockerfile for new reqs
- Refactor footer image processing to improve font loading and add right-alignment for date/time display

**Version 0.0.7-fix2** published on 26.04.2025
- colored logo for better visibility in HA addon overview active (colored)/ not active (b/w)

**Version 0.0.7-fix1** published on 26.04.2025
- fixing image build - submodule fetching

**Version 0.0.7** published on 07.04.2025
- fixing addon config to use the HA config for trmnl server

**Version 0.0.6** published on 04.04.2025
- move add on to ohAnd's addon collection
  
**Version 0.0.5** published on 26.02.2025
- extend HA addon settings
  
**Version 0.0.4-fix3** published on 26.02.2025
- fix logging
  
**Version 0.0.4-fix2** published on 25.02.2025
- fix footer adding

**Version 0.0.4-fix1** published on 25.02.2025
- fix generate certifacte and key for SSL
  
**Version 0.0.4** published on 25.02.2025
- small bugfixes

**Version 0.0.3** published on 17.02.2025
- configurable timezone
  
**Version 0.0.2** published on 09.02.2025
- first runnable release

**Version 0.0.1** published on 04.02.2025
- inital start
