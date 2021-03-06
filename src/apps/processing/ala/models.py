from django.db import models
from apps.common.models import AbstractFeature, AbstractObservation


class SamplingFeature(AbstractFeature):
    # Ala doesn't have geometry value to the yet - to be added in future
    geometry = None


class Observation(AbstractObservation):
    # TODO: migrate this to general Observation model

    # NOTE: see parent class for more information
    feature_of_interest = models.ForeignKey(
        SamplingFeature,
        help_text="Weather station where the observation was taken.",
        related_name='observations',
        editable=False
    )

    class Meta:
        get_latest_by = 'phenomenon_time_range'
        ordering = ['-phenomenon_time_range', 'feature_of_interest', 'procedure',
                    'observed_property']
        unique_together = (('phenomenon_time_range',
                            'observed_property', 'feature_of_interest',
                            'procedure'),)

