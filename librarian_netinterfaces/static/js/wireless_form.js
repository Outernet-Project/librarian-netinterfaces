// Generated by CoffeeScript 1.10.0
var indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

(function(window, $) {
  var NORTH_AMERICA, form, generateOptions, submitForm, togglePassword, updateChannels, url;
  NORTH_AMERICA = ['US', 'CA'];
  form = $('#wireless-form');
  url = form.attr('action');
  generateOptions = function(range) {
    var i, n, options, ref;
    options = [];
    for (n = i = 1, ref = range; 1 <= ref ? i <= ref : i >= ref; n = 1 <= ref ? ++i : --i) {
      options.push("<option value=\"" + n + "\">" + n + "</option>\n");
    }
    return options.join();
  };
  updateChannels = function() {
    var channelField, country, countryField, current, options, range;
    countryField = $('#country');
    channelField = $('#channel');
    country = countryField.val();
    current = channelField.val();
    range = indexOf.call(NORTH_AMERICA, country) >= 0 ? 11 : 13;
    if (current > range) {
      current = range;
    }
    options = generateOptions(range);
    return (channelField.html(options)).val(current);
  };
  togglePassword = function() {
    var hasSecurity, passwordField, passwordWrapper, securityField;
    securityField = $('#security');
    passwordField = $('#password');
    passwordWrapper = passwordField.parents('p.o-field');
    hasSecurity = securityField.val() !== '0';
    return passwordWrapper.toggle(hasSecurity);
  };
  submitForm = function(e) {
    var res;
    e.preventDefault();
    res = $.post(url, form.serialize());
    res.done(function(data) {
      form.html(data);
      ($(window)).trigger('wireless-updated');
      (form.parents('.o-collapsible-section')).trigger('remax');
      togglePassword();
      return updateChannels();
    });
    return res.fail(function() {
      return form.prepend(errorMessage);
    });
  };
  form.on('change', '#security', togglePassword);
  form.on('change', '#country', updateChannels);
  form.on('submit', submitForm);
  togglePassword();
  return updateChannels();
})(this, this.jQuery);