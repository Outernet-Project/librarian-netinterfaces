((window, $, templates) ->
  NORTH_AMERICA = ['US', 'CA']

  errorMessage = templates.dashboardPluginError
  section = $ '#dashboard-netinterfaces'
  formContainer = null
  form = null
  modeForm = null
  url = null

  resizeSection = () ->
      section.trigger 'remax'
      return


  generateOptions = (range) ->
    options = []
    for n in [1..range]
      options.push "<option value=\"#{n}\">#{n}</option>\n"
    return options.join()


  updateChannels = () ->
    countryField = $ '#country'
    channelField = $ '#channel'
    country = countryField.val()
    current = channelField.val()
    range = if country in NORTH_AMERICA then 11 else 13
    if current > range
      current = range
    options = generateOptions range
    (channelField.html options).val current
    return


  togglePassword = () ->
    securityField = $ '#security'
    passwordField = $ '#password'
    passwordWrapper = passwordField.parents 'p.o-field'
    hasSecurity = securityField.val() isnt '0'
    passwordWrapper.toggle hasSecurity
    if not hasSecurity
      passwordField.val ''
    resizeSection()
    return


  submitForm = (e) ->
    e.preventDefault()
    res = $.post url, form.serialize()
    res.done (data) ->
      formContainer.html data
      ($ window).trigger 'wireless-updated'
      initPlugin()
      return
    res.fail () ->
      form.prepend errorMessage
      return
    return


  toggleSwitch = () ->
    select = $ @
    modeForm.submit()


  switchMode = (e) ->
    e.preventDefault()
    res = $.get url, modeForm.serialize()
    res.done (data) ->
      formContainer.html data
      initPlugin()
      return
    res.fail () ->
      form.prepend errorMessage
      return
    return


  initPlugin = (e) ->
    formContainer = section.find '.wireless-settings'
    form = section.find '#wireless-form'
    modeForm = section.find '#mode-form'
    url = form.attr 'action'
    form.on 'change', '#security', togglePassword
    form.on 'change', '#country', updateChannels
    form.on 'submit', submitForm
    modeForm.on 'change', '#mode', toggleSwitch
    modeForm.on 'submit', switchMode
    button = modeForm.find 'button'
    button.hide()

    togglePassword()
    updateChannels()

  section.on 'dashboard-plugin-loaded', initPlugin

)(this, this.jQuery, this.templates)
