-- Creates a trigger that decreases the quantity of an item
-- after adding a new order. Quantity can be negative
DELIMITER // ;
DROP TRIGGER IF EXISTS `update_qty`//
CREATE TRIGGER `update_qty`
AFTER INSERT 
ON orders
FOR EACH ROW
BEGIN
UPDATE items 
SET 
    quantity = quantity - NEW.number
WHERE
    name = NEW.item_name;
END//
DELIMITER ; //
