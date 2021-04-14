"""This module retrieves and converts information from the database."""

from typing import Any, Dict, List

from booking_api.database.database_structure import Hotel, session


class DBExport:
    """Retrieve information from the database."""

    def to_json(self, objects_list: List[Any]):
        """Make from List[cls object] jsonify structure List[Dict]."""
        json_list = []
        for cls_object in objects_list:
            temp_dict = cls_object.to_dict()
            temp_dict.pop('_sa_instance_state', None)
            json_list.append(temp_dict)

        return json_list

    def get_all_hotels(self, args: Dict):
        """Get all hotels."""
        hotels = session.query(Hotel).all()
        return self.to_json(hotels)
