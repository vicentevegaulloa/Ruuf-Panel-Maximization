def maxPanels(panel_width, panel_height, roof_width, roof_height):
    # Base case: If the panel is larger than the roof, it cannot be placed
    cannot_fit_portrait = (panel_width > roof_width or panel_height > roof_height)
    cannot_fit_landscape = (panel_height > roof_width or panel_width > roof_height)
    if cannot_fit_portrait and cannot_fit_landscape:
        return 0

    # Recursive case: Place panels in the roof and the remaining sections
    def place_panels(panel_w, panel_h, section_w, section_h):
        # Calculate the number of panels that can be placed in the section
        panels_across = section_w // panel_w
        panels_down = section_h // panel_h
        panels_placed = panels_across * panels_down

        if panels_placed == 0:
            return 0

        # Calculate the remaining area in the section
        right_section_width = section_w - (panels_across * panel_w)
        right_section_height = section_h
        bottom_section_width = section_w
        bottom_section_height = section_h - (panels_down * panel_h)
        
        right_section_area = right_section_width * right_section_height
        bottom_section_area = bottom_section_width * bottom_section_height

        # Recursive call to place panels in the biggest remaining section
        if right_section_area >= bottom_section_area and right_section_area > 0:
            additional_panels = maxPanels(panel_width, panel_height, right_section_width, right_section_height)
        elif bottom_section_area > 0:
            additional_panels = maxPanels(panel_width, panel_height, bottom_section_width, bottom_section_height)
        else:
            additional_panels = 0

        # Return the total number of panels placed
        return panels_placed + additional_panels

    # Place panels in the roof in starting with portrait orientation
    portrait_count = place_panels(panel_width, panel_height, roof_width, roof_height)
    # Place panels in the roof in starting with landscape orientation
    landscape_count = place_panels(panel_height, panel_width, roof_width, roof_height)

    # Return the maximum number of panels placed
    return max(portrait_count, landscape_count)

print(maxPanels(1, 2, 5, 3))  # 7
print(maxPanels(1, 2, 3, 5))  # 7
