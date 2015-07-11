from apps.utils.monitoring import log_time


class ListingFilter(object):

    def __init__(self, request, queryset):
        self.request = request
        self.queryset = queryset
        self._result = self.queryset

    def get_result(self):
        LISTING_FILTERS = (
            ('vegetable', self._apply_vegetable),
            ('active', self._apply_active),
            ('ids', self._apply_ids),)
        for val, func in LISTING_FILTERS:
            key = self.request.GET.get(val)
            if key:
                func(key)
        return self._result

    @log_time
    def _apply_vegetable(self, vegetable):
        self._result = self._result.filter(vegetable=vegetable)

    @log_time
    def _apply_ids(self, ids_str):
        values = [int(r) for r in ids_str.split(',')]
        # self._result = self._result.filter(id__in=values)
        # This is done to duplicate objects if the id is repeated
        # !do not replace with queryset filter function
        self._result = [self._result.get(pk=id) for id in values]

    @log_time
    def _apply_active(self, *args):
        self._result = self._result.active()
        # self._result = [l for l in self._result if l.is_active]
