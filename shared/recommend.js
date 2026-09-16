/* ============================================================================
   Orchid Tree - Room Recommendation Algorithm
   ----------------------------------------------------------------------------
   Filters and sorts available rooms based on predefined priorities and guest count.
   Outputs a maximum of 2 rooms, marking the highest-priority one as "Recommended".
   ========================================================================== */

(function () {
  // --- Configurable Priority Order ------------------------------------------
  var PRIORITIES = {
    "Family Room by the Pool": {
      // Prompt: When guest count is > 4
      ">4": ["ashoka", "mallige", "spatika", "parijata"],
      // Default order (can be modified if <= 4 requires different logic)
      "default": ["ashoka", "mallige", "spatika", "parijata"] 
    },
    "Couple Room": {
      "default": ["tulsi", "bael", "bilva", "datura", "hattimara", "bodhi-tree"]
    }
  };

  /**
   * recommendRooms
   * @param {string} category - e.g., "Family Room by the Pool" or "Couple Room"
   * @param {number} guestCount - Total number of guests
   * @param {Array<string>} availableRoomIds - Array of room IDs that are available for the selected date
   * @returns {Array<Object>} - Array of up to 2 room objects: { id: string, isRecommended: boolean }
   */
  function recommendRooms(category, guestCount, availableRoomIds) {
    var priorityList = [];

    // 1. Determine the appropriate priority list based on category & guests
    if (category.indexOf("Family Room") !== -1) {
      if (guestCount > 4) {
        priorityList = PRIORITIES["Family Room by the Pool"][">4"];
      } else {
        priorityList = PRIORITIES["Family Room by the Pool"]["default"];
      }
    } else if (category.indexOf("Couple Room") !== -1 || category.indexOf("Couple Garden") !== -1) {
      priorityList = PRIORITIES["Couple Room"]["default"];
    } else {
      // Fallback if category doesn't match predefined priorities
      priorityList = availableRoomIds.slice(); 
    }

    // 2. Filter the priority list to keep only the available rooms
    // We iterate through the priority list to preserve the exact configured order
    var availableInPriorityOrder = priorityList.filter(function (roomId) {
      return availableRoomIds.indexOf(roomId) !== -1;
    });

    // 3. Keep only the top 2 available rooms
    var topRooms = availableInPriorityOrder.slice(0, 2);

    // 4. Format output and mark the first one as "Recommended"
    return topRooms.map(function (roomId, index) {
      return {
        id: roomId,
        isRecommended: index === 0
      };
    });
  }

  // Expose module
  window.OrchidRecommend = {
    PRIORITIES: PRIORITIES,
    recommendRooms: recommendRooms
  };
})();