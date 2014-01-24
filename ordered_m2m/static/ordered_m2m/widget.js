(function($) {

  var storage;

  var Storage = function(id) {
    // Storage for the ordering of the M2M widgets
    // happens in a hidden <textarea> containing a
    // JSON dump with every widget's ordering.

    var element;
    var store = {};

    var _read = function() {
      var text = element.text();
      if (text) {
        store = JSON.parse(element.text());
      }
    };

    var _write = function() {
      element.text(JSON.stringify(store));
    };

    var _get = function(field) {
      return store[field];
    };

    var _set = function(field, content) {
      store[field] = content;
      _write();
      return content;
    };

    var __init = function(id) {
      element = $('#' + id);
      _read();
    };

    __init(id);

    return {
      set: _set,
      get: _get
    };
  };

  var OrderedM2M = function(obj) {
    // Controller to track changes to the ordering and
    // keep the storage updated

    var parent;
    var container;
    var select;
    var controls;
    var add;
    var remove;
    var up;
    var down;
    var id = obj.id;
    var field = obj.field;

    var insertUI = function() {
      controls = $('<div class="ordered-m2m-controls">');
      up = $('<a class="ordered-m2m-up">Up</a>');
      down = $('<a class="ordered-m2m-down">Down</a>');
      controls.append(up, down);
      container.append(controls);
    };

    var getOptions = function() {
      return select.find('option');
    };

    var getSelectedOptions = function() {
      return getOptions().filter(':selected');
    };

    var moveUp = function() {
      if (!up.hasClass('active')) {
        return;
      }
      getSelectedOptions().each(function() {
        var element = $(this);
        var prevElement = element.prev();
        if (prevElement.length) {
          element.insertBefore(prevElement);
        }
      });
      saveOrder();
    };

    var moveDown = function() {
      if (!down.hasClass('active')) {
        return;
      }
      getSelectedOptions().each(function() {
        var element = $(this);
        var nextElement = element.next();
        if (nextElement.length) {
          element.insertAfter(nextElement);
        }
      });
      saveOrder();
    };

    var getOrderedIDs = function() {
      var ids = [];
      var options = getOptions();
      for (var i=0; i<options.length; i++) {
        var val = $(options[i]).val();
        val = parseInt(val);
        ids.push(val);
      }
      return ids;
    };

    var orderOptions = function(orderedIDs) {
      var orderedOptions = [];
      var options = getOptions();
      var option;
      var i;
      for (i=0; i<orderedIDs.length; i++) {
        var id = orderedIDs[i];
        option = options.filter('[value="' + id + '"]');
        orderedOptions.push(option);
        option.detach();
      }
      for (i=0; i<orderedOptions.length; i++) {
        option = orderedOptions[i];
        select.append(option);
      }
    };

    var saveOrder = function() {
      storage.set(field, getOrderedIDs());
    };

    var setInitialOrder = function() {
      var orderedIDs = storage.get(field);
      if (orderedIDs !== undefined) {
        orderOptions(orderedIDs);
      }
    };

    var checkButtons = function() {
      var buttons = up.add(down);
      if (!getSelectedOptions().length) {
        buttons.removeClass('active');
      } else {
        buttons.addClass('active');
      }
    };

    var setBindings = function() {
      up.on('click', moveUp);
      down.on('click', moveDown);
      add.on('click', saveOrder);
      remove.on('click', saveOrder);
      select.on('change', checkButtons);
    };

    var init = function() {
      parent = $('.selector').has('#' + id);
      container = parent.find('.selector-chosen');
      select = container.find('select');
      add = parent.find('.selector-add');
      remove = parent.find('.selector-remove');

      insertUI();
      setBindings();
      setInitialOrder();
    };

    init();
  };

  var init = function() {
    // Store the ordering in a hidden field
    var storageID = orderedFilteredSelectMultiple.storageID;
    storage = Storage(storageID);

    // Bind each of the handlers
    var targets = orderedFilteredSelectMultiple.targets;
    targets.forEach(OrderedM2M);
  };

  $(function() {
    // Delay to allow the Filtered Select widget to be built
    setTimeout(init, 1000);
  });

})(jQuery);

