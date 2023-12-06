from src.classes.label_node import LabelNode


class LabelHierarchy:
    def __init__(self):
        self.leaves = []
        self._construct_hierarchy()

    def _construct_hierarchy(self):
        root = LabelNode('Persuasion', [])

        # Level 2
        level_2_ethos = LabelNode('Ethos', [root])
        level_2_pathos = LabelNode('Pathos', [root])
        level_2_logos = LabelNode('Logos', [root])

        # Level 3
        level_3_ad_hominem = LabelNode('Ad Hominem', [level_2_ethos])
        level_3_justification = LabelNode('Justification', [level_2_logos])
        level_3_reasoning = LabelNode('Reasoning', [level_2_logos])

        # Level 4
        level_4_distraction = LabelNode('Distraction', [level_3_reasoning])
        level_4_simplification = LabelNode('Simplification', [level_3_reasoning])

        # Techniques
        t_name_calling = LabelNode('Name calling/Labeling', [level_3_ad_hominem])
        t_doubt = LabelNode('Doubt', [level_3_ad_hominem])
        t_smears = LabelNode('Smears', [level_3_ad_hominem])
        t_reductio_ad_hitlertum = LabelNode('Reductio ad hitlerum', [level_3_ad_hominem])

        t_bandwagon = LabelNode('Bandwagon', [level_2_ethos, level_3_justification])
        t_appeal_to_authority = LabelNode('Appeal to authority', [level_2_ethos, level_3_justification])
        t_glittering_generalities = LabelNode('Glittering generalities (Virtue)', [level_2_ethos])

        t_exaggeration = LabelNode('Exaggeration/Minimisation', [level_2_pathos])
        t_loaded_language = LabelNode('Loaded Language', [level_2_pathos])
        t_flag_waving = LabelNode('Flag-waving', [level_2_pathos, level_3_justification])
        t_appeal_to_fear = LabelNode('Appeal to fear/prejudice', [level_2_pathos, level_3_justification])
        # t_transfer = LabelNode('Transfer', [level_2_pathos, level_2_pathos, t_appeal_to_fear])

        t_slogans = LabelNode('Slogans', [level_3_justification])
        t_repetition = LabelNode('Repetition', [level_2_logos])
        t_intentional_vagueness = LabelNode('Obfuscation, Intentional vagueness, Confusion', [level_2_logos])

        t_straw_man = LabelNode("Misrepresentation of Someone's Position (Straw Man)", [level_4_distraction])
        t_red_herring = LabelNode('Presenting Irrelevant Data (Red Herring)', [level_4_distraction])
        t_whataboutism = LabelNode('Whataboutism', [level_4_distraction, level_3_ad_hominem])

        t_causal_oversimplification = LabelNode('Causal Oversimplification', [level_4_simplification])
        t_black_white_fallacy = LabelNode('Black-and-white Fallacy/Dictatorship', [level_4_simplification])
        t_thought_terminating_cliche = LabelNode('Thought-terminating cliché', [level_4_simplification])

        self.leaves = [
            t_name_calling, t_doubt, t_smears, t_reductio_ad_hitlertum,
            t_bandwagon, t_appeal_to_authority, t_glittering_generalities,
            t_exaggeration, t_loaded_language, t_flag_waving, t_appeal_to_fear,
            # t_transfer,
            t_slogans, t_repetition, t_intentional_vagueness, t_straw_man,
            t_red_herring, t_whataboutism,
            t_causal_oversimplification, t_black_white_fallacy, t_thought_terminating_cliche
        ]

        self.all_nodes = [
            level_2_ethos, level_2_pathos, level_2_logos,
            level_3_ad_hominem, level_3_justification, level_3_reasoning,
            level_4_distraction, level_4_simplification,
            t_name_calling, t_doubt, t_smears, t_reductio_ad_hitlertum,
            t_bandwagon, t_appeal_to_authority, t_glittering_generalities,
            t_exaggeration, t_loaded_language, t_flag_waving, t_appeal_to_fear,
            # t_transfer,
            t_slogans, t_repetition, t_intentional_vagueness, t_straw_man,
            t_red_herring, t_whataboutism,
            t_causal_oversimplification, t_black_white_fallacy, t_thought_terminating_cliche
        ]

    def get_leaves(self):
        return self.leaves

    def get_parent_labels_flat(self, node: LabelNode) -> list[str]:
        all_parents: list[LabelNode] = [node]
        nodes_to_handle: list[LabelNode] = [node]

        while nodes_to_handle:
            curr_node = nodes_to_handle.pop()
            for curr_parent in curr_node.parents:

                # If the node is not yet covered and not the root node
                if curr_parent not in all_parents and curr_parent.parents:
                    all_parents.append(curr_parent)
                    nodes_to_handle.append(curr_parent)

        return [n.text for n in all_parents]

    def get_node_by_label(self, lbl: str) -> LabelNode:
        candidates: list[LabelNode] = [n for n in self.all_nodes if n.text == lbl]
        assert len(
            candidates) == 1, f'Expected to find exactly one node with label: {lbl} but found {len(candidates)} instead'
        return candidates[0]
